from django.db import models


class Produit(models.Model):
    ingredient = models.CharField(max_length=100)
