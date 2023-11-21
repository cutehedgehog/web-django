from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import AddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product,
                 quantity=form_data['quantity'],
                 update_quantity=form_data['update'])
    return redirect('cart:cart_details')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart_details.html', {'cart': cart})
