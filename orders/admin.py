from django.contrib import admin

# Register your models here.

from .models import Items, Orders

myModels = [Items, Orders]

admin.site.register(myModels)
