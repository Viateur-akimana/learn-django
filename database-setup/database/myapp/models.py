from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField() 
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)