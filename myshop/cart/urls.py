from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details, name='cart_details'),
    path('add_product/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove_product/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
