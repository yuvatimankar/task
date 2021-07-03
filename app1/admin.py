from django.contrib import admin
from . models import Client, Constituency, Login, service
# Register your models here.

class App1Admin(admin.ModelAdmin):
    list_display=('adminid','username','password','contact','contype')

    admin.site.register(Login)
    admin.site.register(Constituency)
    admin.site.register(service)
    admin.site.register(Client)
