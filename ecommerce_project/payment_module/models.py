from django.db import models
from django.contrib.auth.models import User
from product_module.models import Product
import uuid

class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4,editable=False) 
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()
    city= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    payment_date = models.DateTimeField()
    total_amount = models.FloatField()


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_amount = models.FloatField()
    def __str__(self):
        return f"{self.id}"
