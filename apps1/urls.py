from django.urls import path
from . import views

urlpatterns = [
    path("", views.createac, name="create-account"),   
    path("login/",views.login,name="login"),
    path("home/",views.home,name="home"),
    path("deposite/",views.deposite,name="deposite"),
    path("withdraw/",views.withdraw,name="withdraw"),
    path("sucess/",views.sucess,name="sucess"),
    path("reset/",views.reset,name="reset"),
]