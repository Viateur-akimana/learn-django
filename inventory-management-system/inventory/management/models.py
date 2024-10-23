from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    quantity=models.IntegerField(max_length=100)
    supplier=models.CharField(max_length=1000)
    def __str__(self):
        return self.name