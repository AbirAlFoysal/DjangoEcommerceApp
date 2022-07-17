from pyexpat import model
from re import template
from django.shortcuts import render
from requests import request
from sqlalchemy import null
from .models import Cartitems, Customer, Product, Cart
from django.http import JsonResponse
import json
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    template_name = "ProductDetail.html"
    def d_cart(request):
        cart = 0
        if request.user.is_authenticated:
            customer = request.user.customer
            cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
            cartitems = cart.cartitems_set.all()
        products = Product.objects.all()
        return render(request, 'ProductDetail.html', {'products': products, 'cart':cart})





def store(request):
    cart = 0
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    products = Product.objects.all()
    return render(request, 'store.html', {'products': products, 'cart':cart})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'checkout.html', {'cartitems' : cartitems, 'cart':cart})




def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    

    return JsonResponse("Cart Updated", safe = False)


def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)



def bkashpay(request):
    return render(request, 'bkashpay.html',)

def cod(request):
    return render(request, 'cod.html',)
    