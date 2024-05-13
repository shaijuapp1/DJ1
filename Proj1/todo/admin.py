from django.contrib import admin
from .models import TodoItem 
from .WebDoc import WebDoc 
from .WebDocTag import WebDocTag 


admin.site.register(TodoItem)
admin.site.register(WebDoc)
admin.site.register(WebDocTag)

