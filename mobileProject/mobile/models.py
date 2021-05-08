from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=120)
    price=models.FloatField()
    specs=models.CharField(max_length=150)
    image=models.ImageField(upload_to="images/")


    def __str__(self):
        return self.product_name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    choices=(
        ("ordered","ordered"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=choices,default="ordered")
    user=models.CharField(max_length=120)
