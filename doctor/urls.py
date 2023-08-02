from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('my_appointments',my_appointments,name='my_appointments'),
    path('my_scheduled_appointments',my_scheduled_appointments,name='my_scheduled_appointments'),
    path('my_rejected_appointments',my_rejected_appointments,name='my_rejected_appointments'),
    path('rescheduled_appointments/<int:id>',rescheduled_appointments,name='rescheduled_appointments'),
    path('update_appointment/<int:id>/<str:status>',update_appointment,name='update_appointment'),
    path('doctor_view',doctor_view,name='doctor_view'),
    path('doctor_profile',doctor_profile,name='doctor_profile'), 
      
]