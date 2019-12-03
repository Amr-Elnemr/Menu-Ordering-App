from django.urls import path

from . import views


urlpatterns = [
    path("",                 views.index,            name = "index"),

    # path("mycart",           views.mycart,           name = "mycart"),
    path("MyCart",           views.MyCart.as_view(), name = "mycart"),

    path("register",         views.register,         name = "register"),

    # path("home",             views.home,             name = "home"),
    path("home",             views.Home.as_view(),    name = "home"),

    # path("signin",           views.signin,           name = "signin"),
    path("signin",           views.SignIn.as_view(), name = "signin"),

    path("signout",          views.signout,          name = "signout"),
    path("add_to_cart",      views.add_to_cart,      name = "add_to_cart"),
    path("remove_from_cart", views.remove_from_cart, name = "remove_from_cart"),

    # path("test",     views.test,    name = "test") #used once to add data using beautiful soap
]
