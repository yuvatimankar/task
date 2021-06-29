from django.contrib import admin
from . models import Login
# Register your models here.

class App1Admin(admin.ModelAdmin):
    list_display=('adminid','username','password','contact')

    admin.site.register(Login)