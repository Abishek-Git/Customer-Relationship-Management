from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import DateTimeField, EmailField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField( max_length=50, null=True)
    email = models.EmailField(null=True, max_length=254)
    profile_pic = models.ImageField(default = "PIC_Pass_size.jpg" , null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or str(self.user)


class Tags(models.Model):
    TAGS_ALL = (('outdoor', 'outdoor'),
                ('Indoor', 'Indoor'),
                ('Furniture', 'Furniture'),
                ('Electronics', 'Electronics'))
    name = models.CharField(max_length=50, null = True, choices= TAGS_ALL)

    def __str__(self):
        return self.name


class Product(models.Model):
    CHOICES = (('Snack','Snack'),
               ('FastFood', 'FastFood'),
               ('Drink','Drink'),
               ('Games', 'Games'))
    name = models.CharField( max_length=50, null=True)
    price = models.CharField( max_length=50, null=True)
    category = models.CharField( max_length=200, blank=True,  null = True , choices= CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    tag_name = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Pending','Pending'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'))

    Product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True )
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, choices= STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Product.name