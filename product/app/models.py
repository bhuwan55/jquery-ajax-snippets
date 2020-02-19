from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    price =  models.PositiveIntegerField()
    stock = models.CharField(max_length=50)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return (self.name)

class Order(models.Model):
    order_id = models.CharField(max_length=50,unique=True)
    total_cost = models.DecimalField(max_digits=10,decimal_places=2)
    product_list = models.ManyToManyField('OrderedProducts')

class OrderedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

