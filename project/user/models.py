from django import db
from django.db import models
from django.core.validators import int_list_validator

# Create your models here.
class Company(models.Model):
    comp_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=25)
    company_domain = models.CharField(max_length=25)
    company_location = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone_no = models.IntegerField()


    class Meta:
        db_table="company"

class Employee(models.Model):
    emp_id=models.BigAutoField(primary_key=True)
    emp_name = models.CharField(max_length=25)
    company_id= models.IntegerField()
    domain=models.CharField(max_length=25)
    ready_to_relocate = models.BooleanField() 
    current_loc=models.CharField(max_length=25)
    resume_link=models.URLField()
    notice_period=models.DateField()
    laidoffdate=models.DateField()


    class Meta:
        db_table="employee"     
