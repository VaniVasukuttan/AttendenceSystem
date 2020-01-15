from django.db import models
from datetime import date

# Create your models here.
#faculty table
class faculty_details(models.Model):
    f_name = models.CharField(max_length=50)
    f_address = models.CharField(max_length=100)
    f_gender = models.CharField(max_length=10)
    f_mobile = models.IntegerField()
    f_email = models.CharField(max_length=50, null=True, blank=True)
    f_designation=models.CharField(max_length=20,default="")
    f_dob=models.DateField()
    f_joiningdate=models.DateField()
    f_bloodgroup=models.CharField(max_length=10,default="")
    f_batch = models.CharField(max_length=10)
    f_qualfication = models.CharField(max_length=10)
    f_password = models.CharField(max_length=50)
    
    
    class Meta:
        db_table = 'faculty_details'
class faculties(models.Model):
    f_name = models.CharField(max_length=50)
    f_address = models.CharField(max_length=100)
    f_gender = models.CharField(max_length=10)
    f_mobile = models.IntegerField()
    f_email = models.CharField(max_length=50, null=True, blank=True)
    f_designation=models.CharField(max_length=20,default="")
    f_dob=models.DateField()
    f_joiningdate=models.DateField()
    f_bloodgroup=models.CharField(max_length=10,default="")
    f_batch = models.CharField(max_length=10)
    f_qualfication = models.CharField(max_length=10)
    f_password = models.CharField(max_length=50)
    
    
    class Meta:
        db_table = 'facultydetails'







