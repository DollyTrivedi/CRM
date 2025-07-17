from django.db import models
from django.db.models import SET_NULL

# Create your models here.
class Customer(models.Model):
    name = models.CharField(null=True)
    phone = models.CharField(null=True)
    email = models.CharField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
#for drop down : CATEGORY and STATUS is create 

class Tag(models.Model):
    name = models.CharField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('OutDoor','OutDoor')
    )
    name =  models.CharField(null=True)
    category = models.CharField(null=True,choices=CATEGORY)
    price = models.FloatField(null=True)
    description = models.CharField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
    )
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    customer = models.ForeignKey(Customer,null=True,on_delete=SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=SET_NULL)
    status = models.CharField(null=True,choices=STATUS)
    note = models.CharField(null=True)
    
    def __str__(self):
        return self.product.name
    