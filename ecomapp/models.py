from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    CAT=((1,'Earphones'),(2,'Speaker'),(3,'Mobile'),(4,'Camera'),(5,'Headset'),(6,'Watch'),(7,'Power Bank'),(8,'Television'),(9,'Laptop'),(10,'Washing Machine'))
    name=models.CharField(max_length=100,verbose_name='Product_Name')
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    pdetail=models.CharField(max_length=300,verbose_name='Product_Detail')
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name           
    

class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)


class Order(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()