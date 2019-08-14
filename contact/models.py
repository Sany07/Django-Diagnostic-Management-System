from django.db import models
from datetime import datetime
# Create your models here.

class Appointment(models.Model):
    name= models.CharField(max_length=50 , null=False)
    phone_no= models.CharField(max_length=11 , null=False)
    message= models.TextField(null=False)
    department= models.CharField(max_length=50 , null=False)
    doctor= models.CharField(max_length=50 , null=False)
    date=models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name