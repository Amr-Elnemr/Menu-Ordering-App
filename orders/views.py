from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Items
from django.db import IntegrityError
import json

# Create your views here.
def home(request):
    return render(request, "Registration.html")

def register(request):
    username = request.POST["username"]
    password = request.POST["psw"]
    try:
        User.objects.create_user(username=username, password=password)
    except IntegrityError:
        return render(request, "Registration.html", {"existing_name": True})
    return redirect(index)

def index(request):
    # return HttpResponse("Project 3: TODO")

    piArray = Items.objects.filter(category='pi')
    paArray = Items.objects.filter(category='pa')
    saArray = Items.objects.filter(category='sa')
    context = {'piArray':piArray, 'paArray':paArray, 'saArray':saArray}
    return render(request, "index.html", context)

def mycart(request):
    return render(request, "mycart.html")
