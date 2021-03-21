from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    is_new = models.BooleanField(default=False, null=True, blank=True)
    size = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)