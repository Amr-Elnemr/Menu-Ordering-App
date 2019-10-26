from django.urls import path

from . import views

urlpatterns = [
    path("",            views.index,      name = "index"),
    path("mycart",      views.mycart,     name = "mycart"),
    path("register",    views.register,   name = "register"),
    path("home",        views.home,       name = "home"),
    path("signin",      views.signin,     name = "signin"),
    path("signout",     views.signout,    name = "signout"),
    path("add_to_cart", views.add_to_cart,name = "add_to_cart"),

    # path("test",     views.test,    name = "test") #used once to add data using beautiful soap
]
