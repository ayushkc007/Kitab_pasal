from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    def __str__(self):
        return f"{self.name}"    

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    def __str__(self):
        return f"{self.name}"

class Author(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    description = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    ISBN = models.BigIntegerField(max_length=13,validators=[RegexValidator(r'^\d{13}$','Number must be 13 digits', 'Invalid number')])
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
        image_tag.short_description = "Product"

    def __str__(self):
        return self.name    


class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField() 