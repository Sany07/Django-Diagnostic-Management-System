from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    branding = models.CharField(max_length=255, default='health')
    phone = models.CharField(max_length=255, default='0111111111')
    copyright = models.CharField(max_length=255, default='© All rights reserved ')
    
    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


class Vision(SingletonModel):
        Title=models.CharField(max_length=20 , null=False, default='Our Vision')
        Subtitle=models.CharField(max_length=30 , null=False)    
        Description=models.TextField(null=False)

        def __str__(self):
            return self.Title

        class Meta:
            verbose_name = "Our Vision"

class Mission(SingletonModel):
        Title=models.CharField(max_length=20 , null=False, default='Our Mission')
        Subtitle=models.CharField(max_length=30 , null=False)    
        Description=models.TextField(null=False )

        def __str__(self):
            return self.Title
        class Meta:
            verbose_name = "Our Mission"  

class Center(SingletonModel):
        Title=models.CharField(max_length=20 , null=False,default='Our Center')
        Subtitle=models.CharField(max_length=30 , null=False)    
        Description=models.TextField(null=False)
        
    
        def __str__(self):
            return self.Title

        class Meta:
            verbose_name = "Our Center"
