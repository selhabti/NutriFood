# Generated by Django 4.1.7 on 2023-03-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produit",
            name="date_creation",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="produit",
            name="ingredient",
            field=models.CharField(max_length=100, null=True),
        ),
    ]