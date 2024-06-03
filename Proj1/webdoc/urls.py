from django.urls import path
from . import views

urlpatterns = [
    

    #path("", views.WebDocList.as_view(), name="webdoc_list"),
    path("view/<int:pk>", views.WebDocView.as_view(), name="webdoc_view"),
    path("new", views.WebDocCreate.as_view(), name="webdoc_new"),
    path("edit/<int:pk>", views.WebDocUpdate.as_view(), name="webdoc_edit"),
    #path("delete/<int:pk>", views.WebDocDelete.as_view(), name="webdoc_delete"),

    path('', views.index, name='index'),
    path('item/<int:id>', views.view, name='item'),

    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('update/', views.update, name='update'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

    path('updateJson/<int:id>', views.updateJson, name='updateJson'),
    path('updateJson/<int:id>', views.updateJson, name='updateJson'),

    path('test/', views.test, name='test'),










]
