from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.IntegerField()
    name = models.CharField()
    phone = models.CharField()
    email = models.CharField()