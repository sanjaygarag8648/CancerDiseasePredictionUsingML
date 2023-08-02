from dataclasses import fields
from .models import *
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password"]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =["address","city","gender","age","mobile"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields =["address","city","gender","mobile","photo","specialization","academicinfo"]