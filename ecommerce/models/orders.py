from django.db import models
from .product import *
from django.contrib.auth.models import User
from .customer import *
import datetime
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default='',null=True)
    phone=models.CharField(max_length=15,default='',null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('-date')
