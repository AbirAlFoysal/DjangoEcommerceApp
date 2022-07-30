from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=50,default="Emon")
    email = models.EmailField(blank=True)
    # def __str__(self):
    #     return self.name


def create_customer(sender, instance, created, *args, **kwargs):
    if created:
        Customer.objects.create(user = instance)
post_save.connect(create_customer, sender = User)


class Product(models.Model):
    name =  models.CharField(max_length=50)
    price = models.FloatField(default=10.55)
    image = models.ImageField()
    detail = models.CharField(max_length=750, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)


    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total

    

    def __str__(self):
        return self.product.name

