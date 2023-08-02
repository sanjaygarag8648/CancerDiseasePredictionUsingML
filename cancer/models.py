from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from pandas import options 
from django.core.validators import RegexValidator

alphanumeric_val = RegexValidator(r'^[0-9a-zA-Z]*$','Only Alphanumeric allowed')
alphabetic_val = RegexValidator(r'^[a-zA-z][a-zA-Z]+[a-zA-Z]*$','Only Alphabets allowed')
mobile_val = RegexValidator(r'^[5-9][0-9]{9}$','Enter 10 digits mobile number')
numeric_val = RegexValidator(r'^[0-9]*$','Only Numbers allowed')
email_val = RegexValidator(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$','Email')
password_val = RegexValidator(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$','a password must be eight characters including one uppercase letter, one special character and alphanumeric characters')

gender_choices = (("male","Male"),("female","Female")) 
specialization_choices = (("gastroenterologist","gastroenterologist"),("Hematologist-oncologist","Hematologist-oncologist"),("Thoracic-oncologists","Thoracic-oncologists"))


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=60,validators=[alphabetic_val])
    mobile = models.BigIntegerField(default=0,validators=[mobile_val])
    age = models.IntegerField(default=0,validators=[numeric_val])
    gender = models.CharField(max_length=12,choices=gender_choices)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=60,validators=[alphabetic_val])
    mobile = models.BigIntegerField(default=0,validators=[mobile_val])
    photo = models.ImageField(upload_to='doctor_photos')
    specialization = models.CharField(max_length=60,choices=specialization_choices)
    gender = models.CharField(max_length=12,choices=gender_choices)
    medicalregno = models.CharField(default=0,max_length=15)
    academicinfo = models.CharField(max_length=1000,default=0)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_date = models.DateField(default=datetime.now)
    appointment_time = models.TimeField()
    appoint_status = models.CharField(default='Pending',max_length=60)
    patient_message  = models.CharField(max_length=260)





    
    