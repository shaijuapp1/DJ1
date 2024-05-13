from django.db import models
from .PageTag import PageTag

class Page(models.Model):
  title = models.CharField(max_length=1000)
  url = models.CharField(max_length=200)
  tag1 = models.ForeignKey(PageTag, on_delete=models.PROTECT,blank=False,null=True, related_name="tag1")
  tag2 = models.ForeignKey(PageTag, on_delete=models.PROTECT,blank=True,null=True,related_name="tag2")
  tag3 = models.ForeignKey(PageTag, on_delete=models.PROTECT,blank=True,null=True,related_name="tag3")
  content = models.TextField()
  det1 = models.TextField(blank=True,null=True)
  d2t2 = models.TextField(blank=True,null=True)


  def __str__(self):
        return self.title