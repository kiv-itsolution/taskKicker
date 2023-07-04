from django.shortcuts import render, redirect
from bitrix24lib.functions.bitrix_token import BitrixToken
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from datetime import datetime, timedelta
import dateutil.parser as dt
from integration_utils.bitrix24.models.bitrix_user_token import BitrixUserToken

AUTH_TOKEN = '1/grvg18g56ktzh1im'
DOMAIN = 'mybitrixbtw.bitrix24.ru'

task_id = 0


# @main_auth(on_start=True, set_cookie=True)
@main_auth(on_start=True, set_cookie=True)
def start(request):
    global task_id
    string = request.POST['PLACEMENT_OPTIONS']
    _dict = json.loads(string)
    hooked_task_id = _dict['taskId']
    task_id = hooked_task_id
    return render(request, 'start.html')


@main_auth(on_cookies=True)
def kick_task(request):
    if request.method == "POST":
        but = BitrixToken(domain=DOMAIN, web_hook_auth=AUTH_TOKEN)
        actual_task = but.call_api_method('tasks.task.get', {'taskId': task_id, 'select': ['DEADLINE']})['result']
        raw_deadline = actual_task['task']
        deadline = raw_deadline['deadline']
        # print(repr(deadline))
        date_time_obj = dt.parse(deadline)
        new_dead_line = date_time_obj + timedelta(hours=1)
        reformat = new_dead_line.strftime('%d.%m.%Y %H:%M:%S')
        # print(reformat)
        but.call_api_method('tasks.task.update', {"taskId": task_id,
                                                  "fields": {
                                                      "DEADLINE": str(reformat)
                                                  }
                                                  })
    return render(request, 'start.html')
