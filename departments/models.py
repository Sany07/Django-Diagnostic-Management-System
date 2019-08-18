from django.db import models

# Create your models here.
class Department(models.Model):
    Name=models.CharField(max_length=50 , null=False)
    Subtitle=models.CharField(max_length=40 , null=False)    
    Description=models.TextField(null=False)
    Image=models.ImageField(upload_to='departments')
    


    def __str__(self):
        return self.Name


class Doctor(models.Model):
    Name=models.CharField(max_length=50 , null=False)   
    Designation=models.CharField(max_length=40 , null=False)    
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Description=models.TextField(null=True)
    Image=models.ImageField(upload_to='doctors')
        
    
    
    def __str__(self):
        return self.Name