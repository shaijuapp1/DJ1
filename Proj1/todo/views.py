from django.shortcuts import render, HttpResponse
from .models import TodoItem



def home(request):
    return render(request, "home.html")

def about(request, *a, **u):
    print(request.user)
    return render(request, "about.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

def doclist(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

def doc(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})