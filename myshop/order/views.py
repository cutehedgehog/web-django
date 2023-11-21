from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from .models import Order
from django.core.exceptions import PermissionDenied
import requests


def create_order(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Permission denied. Sign in first.")

    cart = Cart(request)
    cart_is_empty = len(cart) == 0
    if not cart_is_empty and request.method == 'POST':
        order = Order.objects.create(client=request.user)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     cost=item['cost'],
                                     quantity=item['quantity'])
        cart.clear()
        return render(request, 'order_created.html')

    return render(request, 'create_order.html',
                  {'cart': cart, 'empty': cart_is_empty})


def list_orders(request):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied.")
    orders = Order.objects.all().order_by('client')
    return render(request, 'list_orders.html', {'orders': orders})
