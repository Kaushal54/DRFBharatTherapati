from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)

class Book(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    rating = models.CharField(max_length=255,null=True,blank=True)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
