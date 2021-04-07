from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


# GET request : создается экземпляр формы OrderCreateForm и отображается шаблон
# POST request : проверяет валидность введенных данных, если данные являются допустимыми,
# то для создания нового экземпляра заказа будет использоваться order = form.save()
# GET request: an instance of the OrderCreateForm is created and the template is displayed
# POST request: checks the validity of the entered data, if the data is valid,
# then order = form.save () will be used to create a new instance of the order
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         toy=item['toy'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            # emptying the cart
            cart.clear()
            # запуск асинхронной задачи
            # start an asynchronous task
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
