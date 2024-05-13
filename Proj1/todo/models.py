from django.db import models
from django.urls import reverse  

class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  complected = models.BooleanField(default=False)

  def __str__(self):
        return self.title
  
  def get_absolute_url(self):  
     return reverse('todo_edit', kwargs={'pk': self.pk})
