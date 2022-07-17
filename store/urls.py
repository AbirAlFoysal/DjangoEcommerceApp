from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('store', views.store, name = 'store'),
    path('', views.store, name = 'store'),
    path('cart', views.cart, name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('bkashpay', views.bkashpay, name = 'bpay'),
    path('cod', views.cod, name = 'cod'),
    path('updatecart', views.updateCart, name = 'updatecart'),
    path('updatequantity', views.updateQuantity, name = 'updatequantity'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name = 'detail'),

]