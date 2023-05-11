from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):  #category model
        return self.category_name  #category add gardha name ma aeuxa 

    class Meta:
        db_table = 'app_category'

class Product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)        
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    quantity = models.IntegerField()
    discount = models.FloatField()
    cod = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_products'
  
