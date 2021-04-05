from django.db import models
from django.urls import reverse


# null - если True, то поле в таблице базы данных может хранить значение null
# blank - если True, то Django позволит занести в поле пустое значение
# db_index - если True, то по текущему полю в таблице будет создан индекс
# default - значение по умолчанию, записываемое в поле, если значение не внесено


class Toy(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название игрушки')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=60, null=True, blank=True, db_index=True, verbose_name='Ссылка')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(null=True, verbose_name='Количество')  # Количество товара
    available = models.BooleanField(default=True, verbose_name='В наличии')  # Доступность товара
    created = models.DateTimeField(auto_now_add=True, null=True, db_index=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    typ = models.ForeignKey('Typ', null=True, on_delete=models.PROTECT, verbose_name='Тип игрушки')

    # Опции модели Toy
    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'
        ordering = ['name']
        index_together = (('id', 'slug'),)

    # Метод представления поля name ввиде строки
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys:toy_detail', args=[self.id, self.slug])


class Typ(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название типа игрушки')
    slug = models.SlugField(max_length=200, null=True, db_index=True, unique=True, verbose_name='Ссылка')

    # Опции модели Typ
    class Meta:
        verbose_name = 'Тип игрушки'
        verbose_name_plural = 'Типы игрушек'
        ordering = ['name']

    # Метод представления поля name ввиде строки
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys:toys_by_type', args=[self.slug])
