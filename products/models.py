
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Distributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='distributor_profile')
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} by {self.distributor.name}'
