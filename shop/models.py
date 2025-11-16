from django.db import models

# Create your models here.
class Product(models.Model): #inheriting the models.Model class
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()

