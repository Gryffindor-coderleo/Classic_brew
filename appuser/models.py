from django.db import models

# Create your models here.
class food_order(models.Model):
    u_id=models.CharField(max_length=200)
    or_img=models.ImageField()
    or_name=models.CharField(max_length=200)
    or_price=models.IntegerField()
    or_adrs=models.CharField(max_length=200)
    or_ph=models.CharField(max_length=200)

   