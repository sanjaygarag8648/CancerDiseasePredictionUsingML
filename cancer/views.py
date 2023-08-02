from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *

# Create your views here.
# Patient
def about(request):
    return render(request,'about.html')

def change_password_success(request):
    return render(request,'change_password_success.html')

def appoinment(request,id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        appoinment = Appointment()
        appoinment.patient = request.user.patient
        appoinment.doctor = doctor
        appoinment.appointment_date = request.POST['appointment_date']
        appoinment.appointment_time = request.POST['appointment_time']
        appoinment.patient_message = request.POST['message']
        appoinment.save()
        messages.info(request,'Appointment Request Sent Successfully')
        return redirect('/')
    else:
        return render(request,'appoinment.html',{'doctor':doctor})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        sender = settings.EMAIL_HOST_USER
        message1 = "Name: "+name+" Email: "+email+" Phone: "+phone+" Message: "+message
        send_mail(subject,message1,sender,["cancerdiseaseprediction@gmail.com"])
        messages.info(request,'Contact Details sent successfully')
        return redirect('/')
        
    else:
        return render(request,'contact.html')

def doctorsingle(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,'doctor-single.html',{'doctor':doctor})

def doctor(request):
    specialization_choices = ["gastroenterologist","Hematologist-oncologist","Thoracic-oncologists"]
    doctors = Doctor.objects.all()
    return render(request,'doctor.html',{'doctors':doctors,'specialization_choices':specialization_choices})

def patient_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.patient,appoint_status='Pending')
    return render(request,'patient_appointments.html',{'appointments':appointments})

def patient_scheduled_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.patient,appoint_status='Accepted')
    return render(request,'patient_scheduled_appointments.html',{'appointments':appointments})

def patient_rejected_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.patient,appoint_status='Rejected')
    return render(request,'patient_rejected_appointments.html',{'appointments':appointments})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            try:
                patient = Patient.objects.get(user=user)
            except Patient.DoesNotExist:
                messages.info(request,"You can not login as a Patient !!!")
                return redirect('userlogin')
            if user.is_active:
                login(request,user)
                request.session['user_id'] = user.id
                messages.info(request,"Logged-in Successfully...")
                return redirect('index')
            else:
                return HttpResponse('Account not active')
        else:
            messages.info(request,"Enter correct User Name and Password !!!")
            return redirect('userlogin')
    else:
        
        return render(request,'userlogin.html')

def userlogout(request):
    request.session.flush()
    logout(request)
    return redirect('index')

def userregister(request):
    user_form = UserForm()
    patient_form = PatientForm()
    gender_choices = ("male","female")
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        patient_form = PatientForm(request.POST)
        try:
            user = User.objects.get(username=request.POST['email'])
            if user:
                messages.info(request,'This Email is Already Registered with us')
                return redirect('userlogin')
        except User.DoesNotExist:
            print('Email Does not Exist')
            if user_form.is_valid() and patient_form.is_valid:
                user_instance = User.objects.create_user(username=request.POST['email'],first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],password=request.POST['password'])
                user_instance.save()
                patient_instance = Patient.objects.create(user=user_instance,address=request.POST['address'],age=request.POST['age'],
                mobile=request.POST['mobile'],
                city=request.POST['city'],gender=request.POST['gender'])
                patient_instance.save()
                messages.info(request,'User Registered Successfully')
                return redirect('userlogin')
            else:
                print(user_form.errors)
                print(patient_form.errors)
                return render(request,'userregister.html',{'user_form':user_form,'patient_form':patient_form,'gender_choices':gender_choices})
    else:
        return render(request,'userregister.html',{'user_form':user_form,'patient_form':patient_form,'gender_choices':gender_choices})
    
def patient_view(request):
    patient = Patient.objects.all()
    return render(request,'patient_view.html',{'patient':patient})

def profile(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        patient = Patient.objects.get(user=request.user)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        patient.address = request.POST['address']
        patient.city = request.POST['city']
        patient.gender = request.POST['gender']
        patient.age = request.POST['age']
        patient.mobile = request.POST['mobile']
        patient.save()
        messages.info(request,'User Updated Successfully')
        return redirect('index')
    else:
        return render(request,'profile.html')

def doctorregister(request):
    user_form = UserForm()
    doctor_form = DoctorForm
    specialization_choices = ("gastroenterologist","Hematologist-oncologist","Thoracic-oncologists")
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid:
            user_instance = User.objects.create_user(username=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
            user_instance.save()
            doctor_instance = Doctor.objects.create(user=user_instance,address=request.POST['address'],mobile=request.POST['mobile'],city=request.POST['city'],gender=request.POST['gender'],photo=request.FILES['photo'],specialization=request.POST['specialization'],academicinfo=request.POST['academicinfo'],medicalregno=request.POST['medicalregno'])
            doctor_instance.save()
            messages.info(request,'Doctor Registered Successfully')
            return redirect('doctorlogin')
        else:
            print(user_form.errors)
            print(doctor_form.errors)
            return render(request,'doctorregister.html',{'user_form':user_form,'patient_form':doctor_form,'gender_choices':gender_choices})
    else:
        return render(request,'doctorregister.html',{'user_form':user_form,'patient_form':doctor_form,'specialization_choices':specialization_choices})

def doctorlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            try:
                doctor = Doctor.objects.get(user=user)
            except Doctor.DoesNotExist:
                messages.info(request,'You cannot login as Doctor !!!')
                return redirect('doctorlogin')
            if user.is_active:
                login(request,user)
                request.session['user_id'] = user.id
                messages.info(request,"Logged-in Successfully...")
                return redirect('index')
            else:
                return HttpResponse('Account not active')
        else:
            messages.info(request,"Enter correct User Name and Password !!!")
            return redirect('doctorlogin')
            
    else:
        return render(request,'doctorlogin.html')

def doctordeleteinfo(request,id):
    doctor = Doctor.objects.get(id=id)
    doctor.user.delete()
    messages.info(request,"Doctor Details Deleted Successfully...")
    return redirect('doctorinfo')
    
def doctorinfo(request):
    doctor = Doctor.objects.all()
    return render(request,'doctorinfo.html',{'doctor':doctor})

def patientdeleteinfo(request,id):
    patient = Patient.objects.get(id=id)
    patient.user.delete()
    messages.info(request,"Patient Details Deleted Successfully...")
    return redirect('patientinfo')
    
def patientinfo(request):
    patient = Patient.objects.all()
    return render(request,'patientinfo.html',{'patient':patient})

def specilization_dept(request,dept):
    doctors = Doctor.objects.filter(specialization=dept)
    return render(request,'doctor.html',{'doctors':doctors})

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_superuser:
                if user.is_active:
                    login(request,user)
                    request.session['user_id'] = user.id
                    return redirect('index')
                else:
                    return HttpResponse('Account not active')
            else:
                messages.info(request,'You cannot login as Admin !!!')
                return redirect('adminlogin')

        else:
            messages.info(request,"Invalid Credentials")
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')



def blogsidebar(request):
    return render(request,'blog-sidebar.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def confirmation(request):
    return render(request,'confirmation.html')



def departmentsingle(request):
    return render(request,'department-single.html')

def department(request):
    return render(request,'department.html')


def documentation(request):
    return render(request,'documentation.html')

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def diseaseindex(request):
    return render(request,'diseaseindex.html')





def symptoms(request):
    return render(request,'symptoms.html')

def predict_disease(request):
    return render(request,'predict_disease.html')


    




# Doctor



#Admin

def userinfo(request):
    return render(request,'userinfo.html')

def graphs(request):
    return render(request,'graphs.html')






