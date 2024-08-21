from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.TextField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, upload_to='plants/')
    weather = models.TextField(null=True)
    market_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    tips = models.TextField(null=True)
    management = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body