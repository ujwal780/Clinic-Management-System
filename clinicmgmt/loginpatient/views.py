from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, message, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from clinicmgmt import settings as conf
from django.contrib import messages
from django.contrib.auth.models import User,auth
from loginpatient.models import Appointment,Covid19,PatientRegister,PrescriptionForm
from loginpatient.forms import LoginForm,RegisterForm,AppointmentForm,CovidForm,PRegistrationForm
from django.views.decorators.cache import cache_control
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from datetime import date
from .decorators import  allowed_users, admin_only
import xlwt
from xlwt.Formatting import Borders

# Create your views here.
def login_page(request):
    cname=conf.cname
    if request.method=='GET':
        loginForm=LoginForm()
    else:
        loginForm=LoginForm(request.POST)    
        if loginForm.is_valid():
            userName=loginForm.cleaned_data['username']
            userPassword=loginForm.cleaned_data['passwd']
            try:
                user=auth.authenticate(username=userName,password=userPassword)
                if user is not None:
                    auth.login(request,user)
                    request.session['username']=userName
                    return redirect('dashboard')
                else:
                    messages.info(request,'invalid username and password.... try again')    
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('dashboard') 
    context = {
        'loginForm': loginForm,'company':cname,
        }        
    return render(request, "logindata/login.html",context)  


def register(request):
    cname=conf.cname
    if request.method=='GET':
        registerForm=RegisterForm()
    else:
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            user_name=registerForm.cleaned_data['usrR_name']
            user_email=registerForm.cleaned_data['usrR_email']
            user_fistname=registerForm.cleaned_data['usrR_firstname']
            user_lastname=registerForm.cleaned_data['usrR_lastname']
            user_password=registerForm.cleaned_data['usrR_passwd']
            user_password2=registerForm.cleaned_data['usrR_passwd2']
            try:
                if (user_password==user_password2):
                    if User.objects.filter(username=user_name).exists():
                        messages.warning(request,'User name exists... try another')
                        return redirect('register') 
                    elif User.objects.filter(email=user_email).exists(): 
                        messages.warning(request,'User email exists... try another') 
                        return redirect('register')    
                    else:
                        user=User.objects.create_user(username=user_name,email=user_email,password=user_password,first_name=user_fistname,last_name=user_lastname)
                        user.save() 
                        messages.warning(request,'User email exists... try another') 
                        messages.success(request,'User Created Sucessfully...')
                        return redirect('register') 
                else:
                    messages.info(request,'Password not matching.... try again') 
                    return redirect('register')    
            except:
                return HttpResponse('Invalid header found. here...')
                #return redirect('register')   

    context = {
        'registerForm': registerForm,'company':cname,
        }        
    return render(request, "logindata/register.html",context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')

def dashboard(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username']
        #x=str(datetime.date.now())
        today = date.today() 
        print(today)
        appoint = Appointment.objects.filter(appointment_date=today).count()
        covid= Covid19.objects.filter(date_of_checkup=today).count()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Dashboard",
            "appoint":appoint,
            "covid":covid
            }
        return render(request,"patientviews/dashboard.html",context) 
    else:
        return redirect('login') 

def web_logout(request):
    del request.session['username']
    auth.logout(request)
    return redirect('login')

def appointment(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username'] 


        if request.method == 'GET':
            appointment_form = AppointmentForm()
        else:
            appointment_form = AppointmentForm(request.POST)
            #userdata=request.user.id
            if appointment_form.is_valid():
                uname=appointment_form.cleaned_data['usernm']
                person_name=appointment_form.cleaned_data['pName']
                age = appointment_form.cleaned_data['age']
                sex = appointment_form.cleaned_data['sex']
                aDate = appointment_form.cleaned_data['appointment_date']
                aSess= appointment_form.cleaned_data['appointment_session']
                pMobile = appointment_form.cleaned_data['pMobile']
                message = appointment_form.cleaned_data['p_message']
                saveAppoint=Appointment()
                try:
                    saveAppoint.unname=uname
                    saveAppoint.name=person_name
                    saveAppoint.dob=age
                    saveAppoint.gender=sex
                    saveAppoint.appointment_date=aDate
                    saveAppoint.appointment_session=aSess
                    saveAppoint.mobile=pMobile
                    saveAppoint.message=message
                    saveAppoint.save()
                    messages.info(request,"Data store Sucessfully for appointment conformation we will call you later .......") 
                    return redirect('appointment')                         
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
    
        context = {
            'appointment_form': appointment_form,
            'company':cname,
            'user':user_name,
            'page_title':"Appointement",
            }        
        return render(request,'patientviews/appointment.html',context)
    else:
        return redirect('login')

    

def covid(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username'] 

        if request.method == 'GET':
            form = CovidForm()
        else:
            form = CovidForm(request.POST)
            if form.is_valid():
                uname=form.cleaned_data['usernm']
                name=form.cleaned_data['pName']
                age=form.cleaned_data['age']
                sex=form.cleaned_data['sex']
                address=form.cleaned_data['address']
                date_of_checkup=form.cleaned_data['date_of_checkup']
                pMobile=form.cleaned_data['pMobile']
                weight=form.cleaned_data['weight']
                pulse=form.cleaned_data['pulse']
                blood_pressure=form.cleaned_data['blood_pressure']
                temprature=form.cleaned_data['temprature']
                spo2=form.cleaned_data['spo2']
                symptoms=form.cleaned_data['symptoms']
                comorbidity_existing_disease=form.cleaned_data['comorbidity_existing_disease']
                try:
                    covid_obj=Covid19()
                    covid_obj.unname=uname
                    covid_obj.pName=name
                    covid_obj.age=age
                    covid_obj.sex=sex
                    covid_obj.address=address
                    covid_obj.date_of_checkup=date_of_checkup
                    covid_obj.pMobile=pMobile
                    covid_obj.weight=weight
                    covid_obj.pulse=pulse
                    covid_obj.blood_pressure=blood_pressure
                    covid_obj.temprature=temprature
                    covid_obj.spo2=spo2
                    covid_obj.symptoms=symptoms
                    covid_obj.comorbidity_existing_disease=comorbidity_existing_disease
                    covid_obj.save()              
                    messages.info(request,"Data store Sucessfully for appointment conformation we will call you later .......")
                    return redirect('covid')                         
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
    
        context = {
            'form': form,
            'company':cname,
            'user':user_name,
            'page_title':"Covid-19",
            }        
        return render(request,'patientviews/covid.html',context)
    else:
        return redirect('login')

def change_pass(request):
    if request.session.has_key('username'):
        lname=request.user.first_name 
        fname=request.user.first_name
        cname=conf.cname
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password has been changed successfully!')
                return redirect('changepassword')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            
            'lname':lname,
            'fname':fname,
            "form":form,
            "company":cname,
            "page_title":"Change Password",
            }    
        return render(request, 'patientviews/changepassword.html',context) 
    else:
 
        return redirect('login')  

@login_required(login_url='login')
@admin_only
def appoint_table(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username']
        appoint=Appointment.objects.all()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Appointments Table",
            'appoint':appoint

            }
        return render(request,"adminviews/appoint_table.html",context)  
    else:
        return redirect('login')

@login_required(login_url='login')
@admin_only
def covid_table(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username']  
        covid=Covid19.objects.all()      
        context={'company':cname,
            'user':user_name,
            'page_title':"Covid19",
            "covid":covid
            }
        return render(request,"adminviews/covid_appoint.html",context)
    else:
        return redirect('login')
          
@login_required(login_url='login')
@admin_only
def history(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username']
        person=PrescriptionForm.objects.all()
        context = {
            'company':cname,
            'user':user_name,
            'page_title':"Patient History",
            'data':person,            
            }
        return render(request,"adminviews/history.html",context)  
    else:
        return redirect('login')

@login_required(login_url='login')
@admin_only
def delete_history(request,id):
    if request.method == 'POST':
        pi=PrescriptionForm.objects.get(pk=id)
        pi.delete()
            #message.info(request,"Data Deleted")
    return redirect('history')


@login_required(login_url='login')
@admin_only
def admin_Pregister(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username'] 
        
        if request.method=='GET':
            pregisterForm=PRegistrationForm()
        else:
            pregisterForm=PRegistrationForm(request.POST,request.FILES)
            if pregisterForm.is_valid():
                uname=pregisterForm.cleaned_data['usernm']
                email=pregisterForm.cleaned_data['PR_email']
                fname=pregisterForm.cleaned_data['PR_firstname']
                lname=pregisterForm.cleaned_data['PR_lastname']
                mobile=pregisterForm.cleaned_data['PR_mobile']
                address=pregisterForm.cleaned_data['PR_address']
                photo=pregisterForm.cleaned_data['PR_photo']
                dob=pregisterForm.cleaned_data['PR_dob']
                gender=pregisterForm.cleaned_data['sex']
                patient=PatientRegister()
                try:
                    patient.unname=uname
                    patient.fname=fname
                    patient.lname=lname
                    patient.dob=dob
                    patient.gender=gender
                    patient.mobile=mobile
                    patient.email=email
                    patient.address=address
                    patient.photo=photo
                    patient.save()
                    messages.info(request,"Patient Register Sucessfully.......") 
                    return redirect('admin_Pregister')
                except BadHeaderError: 
                    #pass            
                    return HttpResponse('Invalid header found. here...')
                #return redirect('register')   
        pregisterdata=PatientRegister.objects.all()
        context = {
            'pregisterForm': pregisterForm,'company':cname,'user':user_name,'page_title':"Patients Registration","pregisterdata":pregisterdata,}        
    return render(request, "adminviews/register.html",context)



@login_required(login_url='login')
@admin_only
def delete_data(request):
    if request.session.has_key('username'):
        user_name=request.session['username'] 
        if request.method == 'POST':
            pi=Appointment.objects.all()
            pi.delete()
            #message.info(request,"Data Deleted")
    return HttpResponseRedirect('appointable')

@login_required(login_url='login')
@admin_only
def delete_covid(request):
    if request.session.has_key('username'):
        user_name=request.session['username'] 
        if request.method == 'POST':
            pi= Covid19.objects.all()
            pi.delete()
            #message.info(request,"Data Deleted")
    return HttpResponseRedirect('covidtable')

@login_required(login_url='login')
@admin_only
def delete_register(request,id):
    if request.method == 'POST':
        pi=PatientRegister.objects.get(pk=id)
        pi.delete()
            #message.info(request,"Data Deleted")
    return redirect('admin_Pregister')




def user_prescription(request):
    if request.session.has_key('username'):
        cname=conf.cname
        user_name=request.session['username']
        userdata=request.user.id
        pi=PrescriptionForm.objects.filter(patient =userdata )
       
    context = {
        'company':cname,
        'user':user_name,
        'page_title':"Prescription",
        'Userdata':pi,         
        }        
    return render(request,'patientviews/userprescription.html',context)


def export_appointments_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="appointments.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Appointments')

    # Sheet header, first row
    row_num = 0

    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ['Username','Name', 'Dob', 'Gender', 'Appointment_date','Appointment_session','Mobile','Message', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)

    # Sheet body, remaining rows
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = Appointment.objects.all().values_list('unname','name', 'dob', 'gender', 'appointment_date','appointment_session','mobile','message')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], excel_style)

    wb.save(response)
    return response

def export_prescription_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="presc.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Prescription Details')

    # Sheet header, first row
    row_num = 0

    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ['UserId', 'FirstName','Lastname', 'Checkup_date', 'Mobile','Gender','Age','Prescription', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)

    # Sheet body, remaining rows
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = PrescriptionForm.objects.all().values_list('patient','fname', 'lname','Checkup_date', 'mobile', 'gender','age','precscription')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], excel_style)

    wb.save(response)
    return response

def export_covid_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="covid.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Covid Details')

    # Sheet header, first row
    row_num = 0

    excel_style = xlwt.XFStyle()
    excel_style.font.bold = True
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    excel_style.borders = borders
    columns = ['Username','Patient Name', 'Age','Gender', 'Date of Checkup', 'Mobile','Weight','Pulse','Blood Pressure','Temprature','SPO2','Existing_Disease','Symptoms',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], excel_style)

    # Sheet body, remaining rows
    excel_style = xlwt.XFStyle()
    excel_style.borders = borders
    rows = Covid19.objects.all().values_list('unname','pName','age', 'sex', 'date_of_checkup', 'pMobile','weight','pulse','blood_pressure','temprature','spo2','comorbidity_existing_disease','symptoms')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], excel_style)

    wb.save(response)
    return response



