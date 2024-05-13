from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from django.template import loader

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import WebDoc


class WebDocList(ListView):  
     model = WebDoc

class WebDocView(DetailView):  
     model = WebDoc

class WebDocCreate(CreateView):  
     model = WebDoc 
     fields = ['title', 'content']  
     success_url = reverse_lazy('webdoc_list')  
   
   
class WebDocUpdate(UpdateView):  
    model = WebDoc  
    fields = ['title', 'content']  
    success_url = reverse_lazy('webdoc_list')  


class WebDocDelete(DeleteView):  
    model = WebDoc  
    success_url = reverse_lazy('webdoc_list')    

@login_required(login_url="/accounts/login/")
#@role_required(allowed_roles=["Admin"])
def index(request):

  print("User: " + request.user.username )

  if request.user.groups.filter(name='g1').exists():
     print("in Group 1")
  else:
      print("not in Group 1")


  for i in request.user.groups.all():
    print("Group: " + i.name)
  
  #print("======grps: =======" + request.user.groups.all)

  mymembers = WebDoc.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
                      



def view(request, id):
  mymember = WebDoc.objects.get(id=id)
  template = loader.get_template('item.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

#https://www.w3schools.com/django/django_add_record.php

@login_required(login_url="/accounts/login/")
def add(request):
     template = loader.get_template('add.html')
     return HttpResponse(template.render({}, request))

@login_required(login_url="/accounts/login/")
def addrecord(request):
     x = request.POST['title']
     y = request.POST['content']
     item = WebDoc(title =x, content=y)
     item.save()
     return HttpResponseRedirect(reverse('index'))

#https://www.w3schools.com/django/django_delete_record.php
@login_required(login_url="/accounts/login/")
def delete(request, id):
  member = WebDoc.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

#https://www.w3schools.com/django/django_update_record.php
@login_required(login_url="/accounts/login/")
def update(request, id):
  mymember = WebDoc.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def updaterecord(request, id):
  title = request.POST['title']
  content = request.POST['content']
  member = WebDoc.objects.get(id=id)
  member.title = title
  member.content = content
  member.save()
  return HttpResponseRedirect(reverse('index'))