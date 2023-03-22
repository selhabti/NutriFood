from django.db import models


class Produit(models.Model):
    ingredient = models.CharField(max_length=100,null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
