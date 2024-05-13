from django.db import models
from .WebDocTag import WebDocTag

class WebDoc(models.Model):
  title = models.CharField(max_length=1000)
  url = models.CharField(max_length=200)
  tag1 = models.ForeignKey(WebDocTag, on_delete=models.PROTECT,blank=True,null=True)
  #tag2 = models.CharField(max_length=200)
  #tag3 = models.CharField(max_length=200)
  content = models.TextField()
  det1 = models.TextField()
  d2t2 = models.TextField()