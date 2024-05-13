from django.db import models

class PageTag(models.Model):
  tag = models.CharField(max_length=1000)

  def __str__(self):
        return self.tag
