
    
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products, Cart, CartItem

from .models import Products, Cart, CartItem


def home(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})


def contacts(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    products = Products.objects.all()
    return render(request, 'shop.html', {'products': products})


def blog(request):
    return render(request, 'blog.html')





@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    total = sum(item.subtotal() for item in items)

    return render(request, "cart.html", {
        "items": items,
        "total": total
    })

def shoppingcart(request):
    return render(request, 'shopping-cart.html')


def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()

    subtotal = sum(item.subtotal() for item in items)

    return render(request, "checkout.html", {
        "items": items,
        "subtotal": subtotal,
        "total": subtotal,
    })


def wishlist(request):
    return HttpResponse("heart")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')
from django.shortcuts import get_object_or_404, redirect

def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))
        item.quantity = quantity
        item.save()

    return redirect("cart")


def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("cart")