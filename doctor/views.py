import imp
from django.shortcuts import render,redirect
from cancer.models import *
from cancer.views import appoinment, doctor
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def my_appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user.doctor,appoint_status='Pending')
    return render(request,'doctor/my_appointments.html',{'appointments':appointments})

def my_scheduled_appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user.doctor,appoint_status='Accepted')
    return render(request,'doctor/my_scheduled_appointments.html',{'appointments':appointments})

def my_rejected_appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user.doctor,appoint_status='Rejected')
    return render(request,'doctor/my_rejected_appointments.html',{'appointments':appointments})


def rescheduled_appointments(request,id):
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        appointment.appointment_date = request.POST['appointment_date']
        appointment.appointment_time = request.POST['appointment_time']
        appointment.appoint_status = 'Accepted'
        appointment.save()
        patient_email = appointment.patient.user.email
        sender = settings.EMAIL_HOST_USER
        patient_name = appointment.patient.user.first_name+' '+appointment.patient.user.last_name
        doctor_name = appointment.doctor.user.first_name+' '+appointment.doctor.user.last_name
        doctor_specialization = appointment.doctor.specialization
        email_subject = 'Doctor Appointment Notification'
        email_message = 'Hello '+patient_name+', Your appointment request with Dr.'+doctor_name+'('+doctor_specialization+') on '+ appointment.appointment_date+' '+ appointment.appointment_time +' is scheduled'
        send_mail(email_subject,email_message,sender,recipient_list=[patient_email])
        messages.info(request,'Apppointmnet Rescheduled Successfully and Confirmation message sent to your registred email-id')
        return redirect('my_scheduled_appointments')
    else:
        return render(request,'doctor/rescheduled_appointments.html',{'appointment':appointment})

def update_appointment(request,id,status):
    appoinment = Appointment.objects.get(id=id)
    appoinment.appoint_status = status
    appoinment.save()
    patient_email = appoinment.patient.user.email
    sender = settings.EMAIL_HOST_USER
    appoinment_date = str(appoinment.appointment_date)
    appoinment_time = str(appoinment.appointment_time)
    patient_name = appoinment.patient.user.first_name+' '+appoinment.patient.user.last_name
    doctor_name = appoinment.doctor.user.first_name+' '+appoinment.doctor.user.last_name
    doctor_specialization = appoinment.doctor.specialization
    email_subject = 'Doctor Appointment Notification'
    email_message = 'Hello '+patient_name+', Your appointment request with Dr.'+doctor_name+'('+doctor_specialization+') on '+ appoinment_date+' '+ appoinment_time +' is '+status
    send_mail(email_subject,email_message,sender,recipient_list=[patient_email])
    if status == 'Accepted':
        messages.info(request,'Apppointmnet Scheduled Successfully and Confirmation message sent to your registred email-id')
        return redirect('my_scheduled_appointments')
    else:
        messages.info(request,'Apppointmnet Rejected Successfully and Rejection message sent to your registred email-id')
        return redirect('my_rejected_appointments')

def doctor_view(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor/doctor_view.html',{'doctors':doctors})



def doctor_profile(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        doctor = Doctor.objects.get(user=request.user)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        doctor.address = request.POST['address']
        doctor.city = request.POST['city']
        doctor.gender = request.POST['gender']
        doctor.mobile = request.POST['mobile']
        doctor.specialization = request.POST['specialization']
       
        doctor.medicalregno = request.POST['medicalregno']
        doctor.academicinfo = request.POST['academicinfo']
        doctor.photo = request.FILES['photo']
        doctor.save()
        messages.info(request,'Doctor Updated Successfully')
        return redirect('index')
    else:
        return render(request,'doctor/doctor_profile.html')

