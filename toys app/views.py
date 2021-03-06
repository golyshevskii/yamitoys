from django.shortcuts import render, get_object_or_404
from toys.models import Toy, Typ
from cart.forms import CartAddProductForm # подключение формы для добавления игрушки в корзину; connecting a form to add a toy to the cart


 # метод вывода информации о доступных игрушках; method for displaying information about available toys
def toy_list(request, typ_slug=None):
    toy = Toy.objects.filter(available=True)
    types = Typ.objects.all()
    typ = None
    if typ_slug:
        typ = get_object_or_404(Typ, slug=typ_slug)
        toy = toy.filter(typ=typ)
    context = {'toy': toy, 'typ': typ, 'types': types}
    return render(request, 'toys/toys1.html', context)


# метод отображения сведений об игрушке; method for displaying toy details
def toy_detail(request, id, slug):
    toy = get_object_or_404(Toy, id=id, slug=slug, available=True)
    cart_toy_form = CartAddProductForm()
    context = {'toy': toy, 'cart_toy_form': cart_toy_form}
    return render(request, 'toys/toys1_detail.html', context)
