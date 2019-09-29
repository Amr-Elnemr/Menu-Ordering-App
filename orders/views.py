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

    piArray = Items.objects.filter(category='pi')
    paArray = Items.objects.filter(category='pa')
    saArray = Items.objects.filter(category='sa')
    context = {'piArray':piArray, 'paArray':paArray, 'saArray':saArray}
    return render(request, "index.html", context)

@login_required()
def mycart(request):
    return render(request, "mycart.html")
