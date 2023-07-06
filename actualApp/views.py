from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
import json
from datetime import timedelta
import dateutil.parser as dt
from integration_utils.bitrix24.models.bitrix_user_token import BitrixUserToken

# AUTH_TOKEN = 'webhook'
# DOMAIN = 'your_domain.bitrix24.ru'

task_id = 0
bitrix_user_id = 0


@main_auth(on_start=True, set_cookie=True)
def start(request):
    global task_id, bitrix_user_id
    string = request.POST['PLACEMENT_OPTIONS']
    _dict = json.loads(string)
    hooked_task_id = _dict['taskId']  # Получаем ID задачи на котором развернуто приложение
    bitrix_user_id = request.bitrix_user.bitrix_id  # Получаем ID пользователя
    task_id = hooked_task_id
    return render(request, 'start.html')


@main_auth(on_cookies=True)
def kick_task(request):
    if request.method == "POST":
        # but = BitrixToken(domain=DOMAIN, web_hook_auth=AUTH_TOKEN) - Если хотим авторизацию по хуку
        admin = BitrixUserToken.objects.filter(user__is_admin=True, is_active=True)
        but = admin.all()[0]  # Достаем токен админа

        actual_task = but.call_api_method('tasks.task.get', {'taskId': task_id, 'select': ['DEADLINE']})[
            'result']  # Поиск самой задачи и ее дедлайна
        responsible = int(but.call_api_method('tasks.task.get', {'taskId': task_id, 'select': ['RESPONSIBLE_ID']})[
            'result']['task']['responsibleId'])  # Поиск ответственного за задачу

        if responsible != bitrix_user_id:  # Сверяем ID
            status_string = 'Ой, это не ваша задача, вы не можете ее откинуть('
            return render(request, 'start.html', context={
                                                'status_string': status_string,
                                                })  # При несовпадении ID рендерим главную страницу с ошибкой
        raw_deadline = actual_task['task']
        # print(raw_deadline)
        deadline = raw_deadline['deadline']
        # print(repr(deadline))
        date_time_obj = dt.parse(deadline)
        new_dead_line = date_time_obj + timedelta(hours=1)  # Получаем нужное нам время
        reformat = new_dead_line.strftime('%d.%m.%Y %H:%M:%S')  # Переделываем формат времени под принимаемый битриксом
        # print(reformat)
        but.call_api_method('tasks.task.update', {"taskId": task_id,
                                                  "fields": {
                                                      "DEADLINE": str(reformat)
                                                  }
                                                  })  # Откидываем саму задачу на час
    return render(request, 'start.html')
