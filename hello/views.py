
from queue import Empty
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

    if request.method == "GET":
        return HttpResponseRedirect(reverse("index"))

    name = request.POST["user"]
    password = request.POST["password"]
    #print(request.session)


    if name is "" or password is "":
        return render(request, "hello/index.html", {
            "message": "fields can't be empty!"
        })

    else:
        ans = Userr.objects.filter(name=request.POST["user"])
        if len(ans) == 0:
            return render(request, "hello/index.html",{
                "message" : "User not registered Yet! Please Register "
            })
        else:
            if ans[0].password == request.POST["password"]:
                

                request.session["user_id"] = ans[0].id
                
                return render(request, "hello/index.html", {
                    "message" : "User is logged in with session id:- " + str(request.session["user_id"]),
                    
                })


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


def logout(request):
    try:
        print(request.session["user_id"])
        del request.session['user_id']
        try:
            print(request.session['user_id'])
        except KeyError:
            print("ID does not exists!")

        return render(request, 'hello/index.html', {
        "message": "you're logged out"
    })

    except KeyError:
        return render(request, 'hello/index.html', {
        "message": "you're already logged out"
    })


    
    


                 






