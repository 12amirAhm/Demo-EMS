from django.db import models
import uuid
from django.contrib.auth.models import User




#This class is used to create EMPLOYEE Table.
class Employee(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
   
    class Meta:  
        db_table = "tblemployee"


