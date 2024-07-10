from django.db import models

class userdetails(models.Model):
    username=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    userpassword=models.CharField(max_length=200)
    phone=models.IntegerField()
    address=models.CharField(max_length=200)