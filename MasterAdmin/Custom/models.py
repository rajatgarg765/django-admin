from tabnanny import verbose
# from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name="Book_Category"
        verbose_name_plural="Book_Categories"

    book_category=models.CharField(max_length=100)
    
class Book(models.Model):
    name=models.CharField(max_length=50)
    published_date=models.DateField()
    author=models.CharField(max_length=100)
    is_available=models.BooleanField(
        help_text='Is the book available to buy?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BestSellerBook(models.Model):
    year=models.IntegerField()
    rank=models.CharField(max_length=10)
    

    def model_callable(self):
        return self.book.name
