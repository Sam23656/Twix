from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    availability = models.BooleanField()
    creation_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product_info", args=(self.pk))