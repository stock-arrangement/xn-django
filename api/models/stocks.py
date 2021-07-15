from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_id = models.IntegerField(default=0)
    product_id = models.ForeignKey(to='api.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    # purchase_date = models.DateField()

    class Meta:
        app_label = 'api'

