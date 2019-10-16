from django.db import models

# Create your models here.

class Report(models.Model):
    userid=models.CharField(max_length=20 , null=False)
    report=models.FileField()
    description=models.CharField(max_length=200 , null=True)

    def __str__(self):
        return self.userid



