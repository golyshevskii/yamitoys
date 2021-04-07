from django.db import models
from toys.models import Toy


# создание базы данных для заказов пользователей
# creating a database for user orders
class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(null=True, verbose_name='Почтовый ящик')
    address = models.CharField(max_length=250, verbose_name='Адресс')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')
    paid = models.BooleanField(default=False, verbose_name='Оплата')

    # опции класса Order
    # class options Order
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # строковое представление; string representation
    def __str__(self):
        return 'Заказ {}'.format(self.id)

    # получение общей стоимости купленных игрушек
    # getting the total value of purchased toys
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items', verbose_name='Заказ')
    toy = models.ForeignKey(Toy, on_delete=models.PROTECT, related_name='order_items', verbose_name='Игрушка')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    # строковое представление; string representation
    def __str__(self):
        return '{}'.format(self.id)

    # получение цены за игрушку\ек
    # getting a price for a toy\s
    def get_cost(self):
        return self.price * self.quantity
