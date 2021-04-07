from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static

# список путей, ведущих к приложениям сайта
# list of paths leading to site applications
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),         # путь к страничке администрации сайта; path to the site administration page
    re_path(r'^toys/', include('toys.urls')),     # путь к приложению toys; path to toys app
    re_path(r'^cart/', include('cart.urls')),     # путь к приложению cart; path to cart app
    re_path(r'^orders/', include('orders.urls')), # путь к приложению orders; path to orders app
]

# использование статических файлов(изображения для игрушек), если DEBUG = True
# use static files (images for toys) if DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
