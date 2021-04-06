from .cart import Cart


def cart(request):
    context = {'cart': Cart(request)}
    return context
