from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("about/", views.about, name="about"),
    path('execute/', views.execute_code, name='execute_code'),


]
