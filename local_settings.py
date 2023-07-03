DEBUG = True
ALLOWED_HOSTS = ['*']
from integration_utils.bitrix24.local_settings_class import LocalSettingsClass
APP_SETTINGS = LocalSettingsClass(
        portal_domain='mybitrixbtw.bitrix24.ru',
        app_domain='is_demo.it-solution.ru',
        app_name='is_demo_test',
        salt='df897hynj4b34u804b5n45bkl4b',
        secret_key='sfjbh40989034nk4j4389tfj',
        application_bitrix_client_id='local.64997891630e82.60751549',
        application_bitrix_client_secret='uzgiGxiwXVl74sFrlScFdsS6YyvquNW4sdX0W1zwJ70q7Nh7tF',
        application_index_path='/',
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'is_demo',  # Or path to database file if using sqlite3.
        'USER': 'is_demo',  # Not used with sqlite3.
        'PASSWORD': '123456',  # Not used with sqlite3.
        'HOST': 'localhost',
    },
}
