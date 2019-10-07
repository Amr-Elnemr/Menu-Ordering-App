from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Items
from django.db import IntegrityError
import json

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
    # return HttpResponse("Project 3: TODO")
    print(type(request))
    piArray = Items.objects.filter(category='pi')
    paArray = Items.objects.filter(category='pa')
    saArray = Items.objects.filter(category='sa')
    context = {'piArray':piArray, 'paArray':paArray, 'saArray':saArray}
    return render(request, "index.html", context)

@login_required()
def mycart(request):
    return render(request, "mycart.html")


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
