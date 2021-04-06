from django import forms

# количесво возможного выбора игрушек при помещении игрушки в корзину
# number of possible choice of toys when placing a toy in the cart
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


# форма; form
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
