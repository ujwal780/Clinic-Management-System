from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    unname=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)    
    gender=models.CharField(max_length=50) 
    appointment_date=models.CharField(max_length=50)
    appointment_session=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    class Meta:
        db_table:"appointment"

class Covid19(models.Model):
    unname=models.CharField(max_length=50)
    pName=models.CharField(max_length=50)
    age=models.CharField(max_length=3)    
    sex=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    date_of_checkup=models.CharField(max_length=50)
    pMobile=models.CharField(max_length=50)
    weight =models.CharField(max_length=50)
    pulse =models.CharField(max_length=50)
    blood_pressure=models.CharField(max_length=50)
    temprature =models.CharField(max_length=50)
    spo2=models.CharField(max_length=50)
    comorbidity_existing_disease=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=50)
    class Meta:
        db_table:"covid19"

class PatientRegister(models.Model):
    unname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)    
    gender=models.CharField(max_length=50) 
    mobile=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="photo",null=True)
    class Meta:
        db_table:"p_register"

class PrescriptionForm(models.Model):
    patient=models.ForeignKey(User,on_delete=models.DO_NOTHING) 
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50) 
    Checkup_date=models.DateField(auto_now=False,auto_now_add=True)
    mobile=models.CharField(max_length=10)
    gender=models.CharField(max_length=50) 
    age=models.CharField(max_length=3)
    precscription=models.TextField(max_length=1000)
    class Meta:
        db_table:"Precription"

    def __str__(self):
        return self.fname