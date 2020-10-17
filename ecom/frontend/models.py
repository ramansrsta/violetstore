from django.db import models

# Create your models here.
class ClientRegister(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=150)

class ClientLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=150)

class CartCreator(models.Model):
    product_id = models.CharField(max_length=150)
    client_id = models.CharField(max_length=150)
    total_price = models.IntegerField(max_length=150)
    product_count = models.CharField(max_length=20)


class OrderProduct(models.Model):
    client_id = models.CharField(max_length=150)
    payable_amount = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    checked_by = models.CharField(max_length=150,null=True)


