DEBUG = True
ALLOWED_HOSTS = ['https://751b-46-252-249-158.ngrok-free.app']
from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

APP_SETTINGS = LocalSettingsClass(
        portal_domain='b24-rdg681.bitrix24.ru',
        app_domain='751b-46-252-249-158.ngrok-free.app',
        app_name='is_demo_test',
        salt='df897hynj4b34u804b5n45bkl4b',
        secret_key='sfjbh40989034nk4j4389tfj',
        application_bitrix_client_id='local.64a69adf597e05.30109182',
        application_bitrix_client_secret='VVi2lJtos2Q0rTsajK9WnnqMMN1gS26EPkF7kl60KWsjAsS6kY',
        application_index_path='/',
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'is_demo',  # Or path to database file if using sqlite3.
        'USER': 'postgres',  # Not used with sqlite3.
        'PASSWORD': '123456',  # Not used with sqlite3.
        'HOST': 'localhost',
    },
}
