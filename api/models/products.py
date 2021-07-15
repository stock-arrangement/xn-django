from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    points = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        app_label = 'api'
