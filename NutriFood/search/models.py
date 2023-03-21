from django.db import models


# Create your models here.
class produit(models.Model):
    ingredient = models.CharField(max_length=100)


