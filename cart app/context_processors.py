from .cart import Cart


# контекстный метод принимающий запрос и возвращающий словарь
# context method accepting a request and returning a dictionary
def cart(request):
    context = {'cart': Cart(request)}
    return context
