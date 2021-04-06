from decimal import Decimal
from django.conf import settings
from toys.models import Toy


class Cart(object):
    # инициализируем корзину
    # initialize the cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранение пустой корзины в сессии
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    # добавление игрушки в корзину или обновление ее количества
    # adding a toy to the cart or updating its quantity
    def add(self, toy, quantity=1, update_quantity=False):
        toy_id = str(toy.id)
        if toy_id not in self.cart:
            self.cart[toy_id] = {'quantity': 0, 'price': str(toy.price)}
        if update_quantity:
            self.cart[toy_id]['quantity'] = quantity
        else:
            self.cart[toy_id]['quantity'] += quantity
        self.save()

    def save(self):
        # обновление сессии корзины
        # update the cart session
        self.session[settings.CART_SESSION_ID] = self.cart
        # отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    # удаление игрушки из корзины
    # removing a toy from the cart
    def remove(self, toy):
        toy_id = str(toy.id)
        if toy_id in self.cart:
            del self.cart[toy_id]
            self.save()

    # перебор элементов в корзине и получение игрушек из базы данных
    # iterate over the items in the cart and get toys from the database
    def __iter__(self):
        toy_ids = self.cart.keys()
        # получение объектов toy и добавление их в корзину
        # getting toy objects and adding them to cart
        toys = Toy.objects.filter(id__in=toy_ids)
        for toy in toys:
            self.cart[str(toy.id)]['toy'] = toy

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    # подсчет всех игрушек в корзине
    # counting all toys in the cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    # подсчет стоимости товаров в корзине
    # counting total price in the cart
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        # deleting the cart from a session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
