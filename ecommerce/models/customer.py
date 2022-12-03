from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    full_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.full_name
    
    # def register(self):
    #     self.save()

    # @staticmethod
    # def get_customer_by_email(email):
    #     try:
    #         return Customer.objects.get(email=email)
    #     except:
    #         return False


    # def isExists(self):
    #     if Customer.objects.filter(email = self.email):
    #         return True

    #     return  False

