from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_lenght=20)
    last_name = models.CharField(max_lenght=20)
    address = models.CharField(max_lenght=50)
    zipcode = models.IntegerField(max_lenght=8)
    gender = models.CharField(max_lenght=1)
    salary = models.CharField(max_lenght=3)