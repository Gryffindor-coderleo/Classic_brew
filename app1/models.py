from django.db import models

# Create your models here.
class menu(models.Model):
    dish_name=models.CharField(max_length=200)
    price=models.IntegerField()
    dish_img=models.ImageField()

