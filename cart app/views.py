from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from toys.models import Toy
from .cart import Cart
from .forms import CartAddProductForm


# метод получения запроса и номера игрушки и добавление ее в корзину
# method for receiving the request and the number of the toy and adding it to the cart
@require_POST
def cart_add(request, toy_id):
    cart = Cart(request)
    toy = get_object_or_404(Toy, id=toy_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(toy=toy,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail') # перенаправление к деталям корзины


# метод удаление игрушки из корзины
# method for removing a toy from the cart
def cart_remove(request, toy_id):
    cart = Cart(request)
    toy = get_object_or_404(Toy, id=toy_id)
    cart.remove(toy)
    return redirect('cart:cart_detail')


# детали корзины
# cart details
def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart1.html', context)
