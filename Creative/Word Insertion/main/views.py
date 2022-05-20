from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def general(request, place):
    return render(request, f"main/{place}.html")
