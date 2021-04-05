from django.urls import re_path
from toys.views import toy_list, toy_detail

app_name = 'toys' # имя приложения

# пути к методам из файла views
# paths to methods from the views file
urlpatterns = [
    re_path(r'^$', toy_list, name='all_toys'),
    re_path(r'^(?P<typ_slug>[-\w]+)/$', toy_list, name='toys_by_type'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', toy_detail, name='toy_detail'),
]
