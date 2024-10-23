from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        labels={
            "product_id":"Product Id",
            "name":"Name",
            "price":"Price",
            "quantity":"Quantity",
            "supplier":"Supplier"
        }
        widgets={
            "product_id":forms.NumberInput(attrs={"placeholder":"eg .1","class":"form-control"}),
            "name":forms.TextInput(attrs={"placeholder":"eg.mike","class":"form-control"}),
            "price":forms.NumberInput(attrs={"placeholder":"eg.300","class":"form-control"}),
            "quantity":forms.NumberInput(attrs={"placeholder":"eg.32","class":"form-control"}),
            "supplier":forms.TextInput(attrs={"placeholder":"eg. john","class":"form-control"})
        }
    