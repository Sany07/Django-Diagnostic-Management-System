from django.db import models

# Create your models here.

class Service(models.Model):
    Title=models.CharField(max_length=20 , null=False)
    Description=models.CharField(max_length=100 , null=False)

    def __str__(self):
        return self.Title



class Test(models.Model):
    test=models.CharField(max_length=20 , null=False,help_text="Enter Test Name")
    price= models.FloatField(null=False,help_text="Enter Test Price")
    description=models.CharField(max_length=100 , null=False)

    def __str__(self):
        return self.test


