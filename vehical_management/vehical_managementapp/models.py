from django.db import models


# Create your models here.
class info(models.Model):
    CH=((1,'Two wheeler'),(2,'Three Wheeler'),(3,'Four wheeler'))
    num=models.CharField(max_length=10,verbose_name="vehical number")
    vtype=models.IntegerField(choices=CH,verbose_name="vehical type")
    vmodel=models.CharField(max_length=50,verbose_name="vehical model")
    vdesc=models.CharField(max_length=500,verbose_name="vehical")