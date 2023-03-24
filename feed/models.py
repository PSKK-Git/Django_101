from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity_available=models.CharField(max_length=100)
    image = models.ImageField(upload_to='subpost')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class SubPost(models.Model):
    product = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='subposts')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity_available=models.CharField(max_length=100)
    image = models.ImageField(upload_to='subpost')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners')
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    def __str__(self):
        return self.name

class SubProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subproducts')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subproducts')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name



