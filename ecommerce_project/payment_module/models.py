from django.db import models
from django.contrib.auth.models import User
from product_module.models import Product
import uuid
from django.core.validators import RegexValidator

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
    contact_no = models.BigIntegerField(max_length=10,validators=[RegexValidator(r'^\d{10}$','phone number must be 10 digits', 'Invalid phone number')])
    payment_date = models.DateTimeField()
    total_amount = models.FloatField()


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_amount = models.FloatField()
    shipping_status = models.CharField(max_length=256, choices=[('confirmed', 'confirmed'), ('shipping', 'shipping'),('received', 'received')])
    def __str__(self):
        return f"{self.id}"
