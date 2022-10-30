from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from distutils.command.upload import upload
# Create your models here.
class details(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    ConfirmPassword = models.CharField(max_length=150)

class login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    
def _str_(self):
    return self.name

