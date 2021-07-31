from django.db import models

# Create your models here.
class project(models.Model):
    name =models.CharField(max_length=200)
    des =models.CharField(max_length=200)
    link=models.URLField()
    gitlink=models.URLField()
    
    name1 =models.CharField(max_length=200)
    des1 =models.CharField(max_length=200)
    link1=models.URLField()
    gitlink1=models.URLField()
    def __str__(self):
        return self.name

class certificate(models.Model):
    name =models.CharField(max_length=200)
    des =models.CharField(max_length=200)
    link=models.URLField()
    name1 =models.CharField(max_length=200)
    des1 =models.CharField(max_length=200)
    link1=models.URLField()
    def __str__(self):
        return self.name
