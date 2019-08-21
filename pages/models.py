from django.db import models
from django.urls import reverse

from datetime import datetime

class Page(models.Model):
 	title= models.CharField(max_length =30)
 	content = models.TextField()
 	last_update = models.DateTimeField(default=datetime.now())
 	

 	def __str__(self):
 		return self.title

 	def get_absolute_url(self):
    	  return reverse('page-detail', args=[str(self.id)])



