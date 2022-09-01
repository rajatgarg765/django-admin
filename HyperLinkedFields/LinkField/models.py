from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Author(models.Model):
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author

class BestSeller(models.Model):
    year=models.IntegerField()
    rank=models.CharField(max_length=100)
    book_name=models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_available=models.BooleanField()
    book=models.ForeignKey(BestSeller,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name