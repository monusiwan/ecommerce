from django import forms
from .models.customer import *
from .models.product import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','category','description','image']