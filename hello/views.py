
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Userr

# Create your views here.


def index(request):
    return render(request, "hello/index.html")

def redirect_to_index(request):
    foo = reverse('index')
    print("reversed url :- " + foo)
    return HttpResponseRedirect(foo)

def login(request):
    name = request.POST["user"]
    password = request.POST["password"]
    print(request.POST)

    if name is "" or password is "":
        return render(request, "hello/index.html", {
            "message": "fields can't be empty!"
        })

    else:
        if name == "Prem" and password == "password":
            return render(request, "hello/index.html",{
                "message" : "User is logged in !"
            } )
        else:
            return render(request, "hello/index.html",{
                "message" : "Invalid entry!"
            } )


def register(request):
    if request.method == "GET":
       return render(request, "hello/register.html")
    elif request.method == "POST":
        try:
            print(request.POST)
            foo = Userr.objects.create(name=request.POST["username"], email=request.POST["emailid"], password=request.POST["pass"])
            foo.save()
            return render(request, "hello/register.html", {
                "message": "user created sucessfully"
            })

        except IntegrityError:
            return render(request, "hello/register.html", {
                "message": "User already exists!"
            })

                 






