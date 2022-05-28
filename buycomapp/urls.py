from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('shop/',views.shop),
    path('product_detail/',views.product_detail),
    path('cart/',views.mycart),
    path('checkout/',views.checkout),
    path('contact/',views.contact),
    path('login/',views.login),
    path('loggedout/',views.loggedout),
    path('register/',views.register),
    path('add_to_cart/',views.add_to_cart),
    path('cart_item_quantity/',views.cart_item_quantity),
    path('cart_item_delete/',views.cart_item_delete),
    path('dec_quantity/',views.dec_quantity),
    path('profile/',views.profile),
    path('manage_address/',views.profile),
    path('orders/',views.profile),
    path('manage_address/edit_address/',views.profile),
    path('manage_address/add_address/',views.profile),
    path('manage_address/delete_address/',views.profile),
    path('placed_order_details/',views.placed_order_details),
]