import os
from celery import Celery
from django.conf import settings

# DJANGO_SETTINGS_MODULE для программы командной строки Celery
# DJANGO_SETTINGS_MODULE for Celery command line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pupa.settings')

# экземпляр класса Celery для проекта
# an instance of the Celery class for the project
app = Celery('pupa', broker_pool_limit=1)

# загрузка любой настраиваемой конфигурации из параметров проекта
# load any custom config from project options
app.config_from_object('django.conf:settings')

# Celery автоматически обнаруживает асинхронные задачи для приложений, перечисленных в параметрах INSTALLED_APPS
# Celery automatically detects asynchronous tasks for applications listed in the INSTALLED_APPS parameters
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
