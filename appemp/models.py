from django.db import models

# Create your models here.
class emp_details(models.Model):
    emp_name=models.CharField(max_length=200)
    emp_email=models.CharField(max_length=200)
    emp_password=models.CharField(max_length=200)
    phone=models.IntegerField()
    position=models.CharField(max_length=200)
