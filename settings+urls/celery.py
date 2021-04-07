import os
from celery import Celery
from django.conf import settings

# DJANGO_SETTINGS_MODULE для программы командной строки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pupa.settings')

# экземпляр класса Celery для проекта
app = Celery('pupa', broker_pool_limit=1)

# загрузка любой настраиваемой конфигурации из параметров проекта
app.config_from_object('django.conf:settings')

# Celery автоматически обнаруживает асинхронные задачи для приложений, перечисленных в параметрах INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
