from django.contrib import admin

from .models import Student,Country,City

# Register your models here.
admin.site.register(Student)
admin.site.register(Country)
admin.site.register(City)