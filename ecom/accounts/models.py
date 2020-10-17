from django.db import models
# import os
# from uuid import uuid4

# def rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split('.')[-1]
#         # get filename
#         if instance.pk:
#             filename = '{}.{}'.format(instance.pk, ext)
#         else:
#             # set filename as random string
#             filename = '{}.{}'.format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)
#     return wrapper

# Create your models here.
class AddProductModel(models.Model):
    product_name = models.CharField(max_length=150)
    product_description = models.TextField(max_length=150)
    price = models.CharField(max_length=150)
    #product_image = models.FileField(upload_to=rename('documents/'))
    product_image = models.FileField(upload_to='documents/') #needs to be commented out and the commented one shall be used
    product_added_by = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)