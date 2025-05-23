from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Glamrush(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField(blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  
    image = models.ImageField(upload_to='products/', blank=True, null=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
