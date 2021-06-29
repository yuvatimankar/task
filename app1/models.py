from django.db import models

# Create your models here.
class Login(models.Model):
    adminid=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.adminid