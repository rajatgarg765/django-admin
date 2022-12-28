from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True,blank=True)
    modified_on=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name