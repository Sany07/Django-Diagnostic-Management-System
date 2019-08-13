from django.db import models

# Create your models here.

class Service(models.Model):
    Title=models.CharField(max_length=20 , null=False)
    Description=models.CharField(max_length=100 , null=False)

    def __str__(self):
        return self.Title


class Vision(models.Model):
        Title=models.CharField(max_length=50 , null=False)
        Subtitle=models.CharField(max_length=40 , null=False)    
        Description=models.TextField(null=False)
        Publish=models.BooleanField(default=False)

        def __str__(self):
            return self.Title


class Mission(models.Model):
        Title=models.CharField(max_length=50 , null=False)
        Subtitle=models.CharField(max_length=40 , null=False)    
        Description=models.TextField(null=False)
        Publish=models.BooleanField(default=False)  

        def __str__(self):
            return self.Title
        
class Center(models.Model):
        Title=models.CharField(max_length=50 , null=False)
        Subtitle=models.CharField(max_length=40 , null=False)    
        Description=models.TextField(null=False)
        Publish=models.BooleanField(default=False)
        
    
        def __str__(self):
            return self.Title