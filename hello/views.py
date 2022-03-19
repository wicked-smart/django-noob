from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def display(request):
    name = request.POST["foo"]
    print(name)
    if name is "":
        return render(request, "hello/index.html", {
            "message": "fields can't be empty!"
        })

    else:
        return render(request, "hello/index.html", {
            "name": name
        })






