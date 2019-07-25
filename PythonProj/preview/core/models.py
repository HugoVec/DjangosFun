from django.db import models
# Create your models here.


class DKs(models.Model):
    name = models.CharField(max_length=90)


class Client(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=90)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)


