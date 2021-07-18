from django.contrib import admin
from . models import Client, Constituency, Login, service,Plan,Department,DepContact,Remark,Staff,Inward,Outward,Hotel,Reservation,ReservationView,FlightEntry
    


# Register your models here.

class App1Admin(admin.ModelAdmin):
    list_display=('adminid','username','password','contact','contype')

    admin.site.register(Login)
    admin.site.register(Constituency)
    admin.site.register(service)
    admin.site.register(Client)
    admin.site.register(Plan)
    admin.site.register(Department)
    admin.site.register(DepContact)
    admin.site.register(Remark)
    admin.site.register(Staff)
    admin.site.register(Inward)
    admin.site.register(Outward)
    admin.site.register(Hotel)
    admin.site.register(Reservation)
    admin.site.register(ReservationView)
    admin.site.register(FlightEntry)