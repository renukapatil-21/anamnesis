from typing import Counter
from django.db import models
from datetime import datetime

# Create your models here.
class add(models.Model):
    name = models.CharField(max_length= 50)
    gender = models.CharField(max_length= 10)
    birth_date = models.CharField(max_length= 15)
    phone = models.CharField(max_length= 15)
    blood_group = models.CharField(max_length= 5)
    allergy = models.CharField(max_length= 50)
    major_operation = models.TextField()
    date = models.DateField(default= datetime.today())

    def __str__(self):
        return self.name
        

