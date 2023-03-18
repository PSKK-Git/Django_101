from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    text=models.CharField(max_length=140, blank=False, null=False)
    image=models.ImageField()
    def __str__(self):
        return self.text


from django.db import models

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
