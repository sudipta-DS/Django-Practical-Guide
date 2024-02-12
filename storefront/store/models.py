from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=6,decimal_places=2)

class Collection(models.Model):
    name = models.CharField(max_length=100)
    featured_product = models.ForeignKey('Products',
                                         on_delete=models.CASCADE,
                                         null=True,
                                         related_name='+')

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE) 
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)

class Order(models.Model):
    # Choices
    pending_status = 'P'
    complete_status = 'C'
    failed_status = 'F'

    payment_statuses = [
        (pending_status,'Pending'),
        (complete_status,'Complete'),
        (failed_status,'Failed')
    ]
    # Fields
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1,
                                      choices=payment_statuses,
                                      default=pending_status)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class orderItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.PROTECT)
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
