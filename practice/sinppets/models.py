from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name