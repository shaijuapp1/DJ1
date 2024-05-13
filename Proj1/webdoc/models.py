from django.db import models
from django.urls import reverse  

class WebDoc(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()

  def __str__(self):
        return self.title
  
  def get_absolute_url(self):  
     return reverse('todo_edit', kwargs={'pk': self.pk})
