from django.db import models
import datetime

# Create your models here.
class Login(models.Model):
    adminid=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.adminid

class Constituency(models.Model):
    Conid=models.CharField(max_length=200)
    contype=models.CharField(max_length=25)

    def __str__(self):
        return self.contype

class service(models.Model):
    sid=models.CharField(max_length=200)
    sname=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.sname

class Client(models.Model):
    cid=models.CharField(max_length=50)
    cname=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    fb=models.CharField(max_length=50)
    twitter=models.CharField(max_length=50)
    youtube=models.CharField(max_length=50)
    instagram=models.CharField(max_length=50)
    linkedin=models.CharField(max_length=50)
    whatsapp=models.CharField(max_length=10)
    contype=models.CharField(max_length=50)
    dob=models.DateField(max_length=8)
    image=models.ImageField(upload_to='images')
    planstartdate=models.DateField(max_length=10)
    planenddate=models.DateField(max_length=10)

    def __str__(self):
        return self.cname
