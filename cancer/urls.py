from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('',index,name='index'),
    path('about',about,name='about'),
    
    path('appoinment/<int:id>',appoinment,name='appoinment'),
    path('contact',contact,name='contact'),
    path('userlogin',userlogin,name='userlogin'),

    path('blogsidebar',blogsidebar,name='blogsidebar'),
    path('blogsingle',blogsingle,name='blogsingle'),
    path('confirmation',confirmation,name='confirmation'),
   
    path('departmentsingle',departmentsingle,name='departmentsingle'),
    path('department',department,name='department'),
    path('doctorsingle/<int:id>',doctorsingle,name='doctorsingle'),
    path('doctor',doctor,name='doctor'),
    path('documentation',documentation,name='documentation'),
    path('service',service,name='service'),
    path('userlogin',userlogin,name='userlogin'),
    path('userregister',userregister,name='userregister'),
    path('userlogout',userlogout,name='userlogout'),
    path('patient_appointments',patient_appointments,name='patient_appointments'),
    path('patient_scheduled_appointments',patient_scheduled_appointments,name='patient_scheduled_appointments'),
    path('patient_rejected_appointments',patient_rejected_appointments,name='patient_rejected_appointments'),
   
    path('change_password_success',change_password_success,name='change_password_success'),
    path('change-password/',auth_views.PasswordChangeView.as_view(
        template_name='change-password.html',
        success_url='/cancer/change_password_success'),
        name='change_password'),
        
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),


    path('profile',profile,name='profile'),
    path('patient_view',patient_view,name='patient_view'),
    path('diseaseindex',diseaseindex,name='diseaseindex'),
    path('symptoms',symptoms,name='symptoms'),
    path('predict_disease',predict_disease,name='predict_disease'),
    path('specilization_dept/<str:dept>',specilization_dept,name='specilization_dept'),
    

# Doctor
    path('doctorregister',doctorregister,name='doctorregister'),
    path('doctorlogin',doctorlogin,name='doctorlogin'),
      
#Admin
    path('doctordeleteinfo/<int:id>',doctordeleteinfo,name='doctordeleteinfo'),
    path('doctorinfo',doctorinfo,name='doctorinfo'),
    path('patientdeleteinfo/<int:id>',patientdeleteinfo,name='patientdeleteinfo'),
    path('patientinfo',patientinfo,name='patientinfo'),
    path('adminlogin',adminlogin,name='adminlogin'),
    path('graphs',graphs,name='graphs'),
]