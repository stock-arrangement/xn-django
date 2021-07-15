from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(default=0)
    recepient_id = models.ForeignKey(to='api.Recipient', on_delete=models.CASCADE)
    product_id = models.ForeignKey(to='api.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        app_label = 'api'
        unique_together = ('recepient_id', 'product_id')
