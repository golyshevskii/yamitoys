from django.contrib import admin
from toys.models import Toy, Typ 


# классы для отображения полей\ссылок\поиска на странице администрации сайта
# classes for displaying fields\links\search on the site administration page
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'available', 'price', 'typ', 'slug', 'created', 'updated']
    list_display_links = ['name', 'available', 'price']
    search_fields = ['name', 'available', 'typ']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Toy, ToyAdmin)


class TypAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Typ, TypAdmin)
