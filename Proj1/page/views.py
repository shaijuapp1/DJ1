from django.shortcuts import render, HttpResponse
from .page import Page

def pagelist(request):
    pagelist = Page.objects.all()
    return render(request, "pagelist.html", {"pagelist" : pagelist})
    #return render(request, "todos.html", {"todos" : items})

def page(request, id):
    page = Page.objects.get(url = id)
    return render(request, "page.html", {"page" : page})
