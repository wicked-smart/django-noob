from django.urls import  path

from . import views


urlpatterns = [
    path("hello", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("", views.redirect_to_index, name="redirect_to_home"),
    path("logout", views.logout, name="logout")
    
]   



