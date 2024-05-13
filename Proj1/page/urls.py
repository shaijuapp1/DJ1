from django.urls import path
from . import views

urlpatterns = [


    path("pagelist/", views.pagelist, name="pagelist"),
    path("page/<str:id>", views.page, name="page"),
    #path("about/", views.about, name="about"),
]
