from django.contrib import admin
from .models import Appointment,Patients


class MyModelAdmin(admin.ModelAdmin):
    
    readonly_fields  = ['date']

admin.site.register(Appointment , MyModelAdmin)  
admin.site.register(Patients)  

