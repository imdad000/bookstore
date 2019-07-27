from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
	book_id=models.CharField(max_length=100,unique=True)
	book_quantity=models.IntegerField(default=0)
	
	def get_absolute_url(self):
		return reverse("bookapp:home_page", kwargs={'pk': self.pk})
