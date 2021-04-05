from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from toys.models import Toy
from .cart import Cart
from .forms import CartAddProductForm


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
    return redirect('cart:cart_detail')


def cart_remove(request, toy_id):
    cart = Cart(request)
    toy = get_object_or_404(Toy, id=toy_id)
    cart.remove(toy)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart1.html', context)
