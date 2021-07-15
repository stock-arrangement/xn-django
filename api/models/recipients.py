from django.db import models

# Create your models here.
class Recipient(models.Model):
    recipient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        app_label = 'api'
