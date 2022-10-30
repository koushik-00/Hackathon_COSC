from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from distutils.command.upload import upload
# Create your models here.

class course(models.Model):
    Coursename=models.CharField(max_length=150)
    CDescription=models.TextField()
    CObjectives=models.TextField()
    COutcomes=models.TextField()
    Cost=models.FloatField()
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    

    
    
def __str__(self):
    return self.name