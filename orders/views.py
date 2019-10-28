from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Items, Orders
from django.db import IntegrityError
# from django.db.models import Sum
# import json

# Create your views here.
def home(request):
    return render(request, "Registration.html")

def signout(request):
    logout(request)
    return redirect(signin)

def signin(request):
    if request.method == 'GET':
        return render(request, 'Login.html', {"no_user":False})
    username = request.POST["username"]
    password = request.POST["psw"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(index)
    return render(request, "Login.html", {"no_user":True})

def register(request):
    username = request.POST["username"]
    password = request.POST["psw"]
    try:
        User.objects.create_user(username=username, password=password)
    except IntegrityError:
        return render(request, "Registration.html", {"existing_name": True})
    return redirect(index)

@login_required()
def index(request):
    piArray = Items.objects.filter(category='pi')
    paArray = Items.objects.filter(category='pa')
    saArray = Items.objects.filter(category='sa')
    NumOfItems = Orders.objects.filter(user_id=request.user.id).count()
    context = {'piArray':piArray, 'paArray':paArray, 'saArray':saArray, "cart_Count":NumOfItems}
    return render(request, "index.html", context)

@login_required()
def mycart(request):
    orders = Orders.objects.filter(user_id = request.user.id)
    Total = 0
    for order in orders:
        Total = Total + order.item_id.price
    context = {'orders': orders, 'total': Total}

    return render(request, "mycart.html", context)

@login_required()
def add_to_cart(request):
    current_user = User.objects.filter(id=request.user.id).get()
    target_item = Items.objects.filter(id=request.POST['item_id']).get()
    new_order = Orders(user_id=current_user, item_id=target_item, status='p')
    new_order.save()
    NumOfItems = Orders.objects.filter(user_id=request.user.id).count()
    return HttpResponse(NumOfItems)

@login_required()
def remove_from_cart(request):
    target_order_id = request.POST['order_id']
    Orders.objects.filter(id=target_order_id).delete()
    return HttpResponse("Item successfully deleted")

### Add to database from Menu via Beautiful Soap ###
# import urllib.request
# import math
# from bs4 import BeautifulSoup
# def test(request):
#     fhand = urllib.request.urlopen('http://www.pinocchiospizza.net/menu.html')
#     html = fhand.read()
#     soap = BeautifulSoup(html, 'html.parser')
#     table = soap('table', class_="foodmenu")[4]#.prettify()sds
#     name_trs = table.find_all(attrs={"style": "text-align: left;"})
#     price_trs = table.find_all(attrs={"width": "25%"})
#     for p in range(len(price_trs)):
#         # i = Items(name="kk", price="8", category="pi").save()
#         Items(name=name_trs[p].get_text(), price=math.ceil(float(price_trs[p].get_text())), category="sa").save()
#         # print(name_trs[p].get_text())
#         # print(price_trs[p].get_text())
#     return HttpResponse(table)
