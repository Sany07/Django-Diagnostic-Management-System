from django.db import models
from datetime import datetime
from django.utils import timezone
from services.models import Test
from departments.models import Doctor
# Create your models here.


class Patients(models.Model):

    SEX = (
    ("Male", "Male"),
    ("Female", "Female"),
)

    name= models.CharField(max_length=50 , null=False)
    phone_no= models.CharField(max_length=11 , null=False)
    age= models.FloatField(null=False)
    sex= models.CharField(max_length=11 , null=False)
    email= models.EmailField(null=True)
    message= models.TextField(null=False)
    date=models.DateTimeField(default=datetime.now, blank=True)
   # sex= models.CharField(max_length=6 ,choices=SEX,default="Male")
    #test= models.ManyToManyField(Test, blank=True, default=None)
   # doctor= models.ManyToManyField(Doctor, blank=True,  default=None)
   # test= models.TextField(null=False)
   # doctor= models.TextField(null=False)
    

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Patient"

class Appointment(models.Model):
    name= models.CharField(max_length=50 , null=False)
    phone_no= models.CharField(max_length=11 , null=False)
    message= models.TextField(null=False)
    department= models.CharField(max_length=50 , null=False)
    doctor= models.CharField(max_length=50 , null=False)
    date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
        