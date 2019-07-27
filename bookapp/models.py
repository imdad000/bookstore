from django.db import models

# Create your models here.
class Book(models.Model):
	book_id=models.CharField(max_length=100,unique=True)
	book_quantity=models.IntegerField(default=0)
