from django.contrib import admin

from .models.orders import Order
from .models.products import Product
from .models.recipients import Recipient
from .models.stocks import Stock

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Recipient)
admin.site.register(Stock)
