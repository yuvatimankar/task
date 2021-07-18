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

class Plan(models.Model):
    pid=models.CharField(max_length=100)
    pname=models.CharField(max_length=50)
    charges=models.CharField(max_length=50)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.pname

class Client(models.Model):
    cid=models.CharField(max_length=50)
    cname=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contactno=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    fb=models.URLField(max_length=50)
    twitter=models.URLField(max_length=50)
    youtube=models.URLField(max_length=50)
    instagram=models.URLField(max_length=50)
    linkedin=models.URLField(max_length=50)
    whatsapp=models.URLField(max_length=10)
    contype=models.CharField(max_length=50)
    dob=models.DateField(max_length=8)
    image=models.ImageField(upload_to='images')
    plantype=models.CharField(max_length=50, null=True)
    planstartdate=models.DateField(max_length=10)
    planenddate=models.DateField(max_length=10)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.cname

class Department(models.Model):
    depid=models.CharField(max_length=20)
    dname=models.CharField(max_length=30)
    contactno=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=200)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.dname

class DepContact(models.Model):
    depcid=models.CharField(max_length=10)
    depid=models.CharField(max_length=20, null=True)
    name=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=30, null=True)
    email=models.EmailField(unique=True, null=True)
    contactno=models.CharField(max_length=10,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Remark(models.Model):
    rid=models.CharField(max_length=20)
    rtype=models.CharField(max_length=50,null=True)
    description=models.TextField(max_length=200)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.rid

class Staff(models.Model):
    sid=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    contact=models.CharField(max_length=10,null=True)
    address=models.TextField(max_length=200)
    email=models.EmailField(unique=True, null=True)
    joiningdate=models.DateField(max_length=10)
    salary=models.CharField(max_length=20)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.sname

class Inward(models.Model):
    ino=models.CharField(max_length=15)
    subject=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='images')
    letterdate=models.DateField(max_length=10)
    recdate=models.DateField(max_length=10)
    receivedbystaff=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    Remark = models.IntegerField(null=True)
    
    def __str__(self):
        return self.ino

class Outward(models.Model):
    outwardno=models.CharField(max_length=15)
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.outwardno

class Hotel(models.Model):
    hid=models.CharField(max_length=10)
    hname=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.hid

class Reservation(models.Model):
    resid=models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    address=models.TextField(max_length=100)
    photo=models.ImageField(upload_to='images')
    adhaarcard=models.CharField(max_length=12)
    refname=models.CharField(max_length=20)
    refcontact=models.CharField(max_length=10)
    datefrom=models.DateTimeField(max_length=10)
    dateto=models.DateTimeField(max_length=10)
    reason=models.TextField(max_length=100)
    contact=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ReservationView(models.Model):
    past=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    checkout=models.TimeField(auto_now=False)
    checkin=models.TimeField(auto_now=False)
    upcoming=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class FlightEntry(models.Model):
    fid=models.CharField(max_length=15)
    From=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    takeoffdate=models.DateTimeField(max_length=10)
    landingdate=models.DateTimeField(max_length=10)
    PNR=models.CharField(max_length=10)
    ticketamt=models.CharField(max_length=10)
    boardingpassimage=models.ImageField(upload_to='images')
    invoiceimage=models.ImageField(upload_to='images')
    journeytype=models.CharField(max_length=10)
    distance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.fid