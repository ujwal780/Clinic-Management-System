from django import forms
#from .models import PatientPrec

SESSIONS = (
    ('', 'Choose...'),
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
    
)


GENDERS = (
    ('', 'Choose...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Username',max_length=10,min_length=4,empty_value=False,required=True)
    passwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=5,empty_value=False,required=True)

class RegisterForm(forms.Form):
    usrR_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_passwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=5,empty_value=False,required=True)
    usrR_passwd2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Your Password'}),label='Re-Enter Password',max_length=10,min_length=5,empty_value=False,required=True)
    usrR_firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your First Name'}),label='Firstname',max_length=50,min_length=5,empty_value=False,required=True)
    usrR_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Last Name'}),label='Lastname',max_length=50,min_length=5,empty_value=False,required=True)
    usrR_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Usename',max_length=15,min_length=4,empty_value=False,required=True)


class AppointmentForm(forms.Form):
    usernm=forms.CharField(widget=forms.TextInput(attrs={'title': 'Type your Username','placeholder': 'Your Usename'}),error_messages = {"key": "USername here..."},label="Username",max_length=50,min_length=1,empty_value=False,required=True)
    pName=forms.CharField(widget=forms.TextInput(attrs={'title': 'Type your name','placeholder': 'Your name'}),error_messages = {"key": "name here..."},label="Name",max_length=50,min_length=4,empty_value=False,required=True)
    age=forms.CharField(label="DOB",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)    
    sex=forms.ChoiceField(label="Gender",choices=GENDERS,required=True)
    appointment_date=forms.CharField(label="Appointment Date",widget=forms.TextInput(attrs={'type': 'date','placeholder': "DD/MM/YYYY"}),max_length=10,min_length=8,empty_value=False,required=True)
    appointment_session=forms.TypedChoiceField(label="Appointment Session",choices=SESSIONS,required=True)
    pMobile=forms.CharField(widget=forms.TextInput(attrs={'type':'number','title':'Enter numbers Only '}),error_messages = {"key": "mobile number here..."},label="Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    p_message=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':1,'style':'height:2.5em;'}),label='Message',max_length=100,min_length=10,empty_value=False,required=False)


class CovidForm(forms.Form):
    usernm=forms.CharField(widget=forms.TextInput(attrs={'title': 'Type your Username','placeholder': 'Your Usename'}),error_messages = {"key": "USername here..."},label="Username",max_length=50,min_length=4,empty_value=False,required=True)
    pName=forms.CharField(label="Patient Name",max_length=50,min_length=4,empty_value=False,required=True)
    age=forms.CharField(label="Patient Age",max_length=3,min_length=1,empty_value=False,required=True)    
    sex=forms.ChoiceField(label="Gender",choices=GENDERS,required=True)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':1,'style':'height:2.5em;'}),label='Address',max_length=100,min_length=10,empty_value=False,required=False)
    date_of_checkup=forms.CharField(label="Date of checkup",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),max_length=10,min_length=8,empty_value=False,required=True)
    pMobile=forms.CharField(label="Patient Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    weight =forms.CharField(label="Patient weight",max_length=3,min_length=1,empty_value=False,required=True)
    pulse =forms.CharField(label="Patient pulse",max_length=3,min_length=1,empty_value=False,required=True)
    blood_pressure=forms.CharField(label="Patient blood pressure",max_length=8,min_length=4,empty_value=False,required=True)
    temprature =forms.CharField(label="Patient temprature ",max_length=3,min_length=1,empty_value=False,required=True)
    spo2=forms.CharField(label="Spo2",max_length=8,min_length=3,empty_value=False,required=True)

    comorbidity_existing_disease = forms.MultipleChoiceField(label="COMORBIDITY / PRE-EXISTING DISEASE",
        choices = (
            ('Blood Pressure', "Blood Pressure"), 
            ('Diabetes', "Diabetes"),
            ('Heart Disease', "Heart Disease"),
            ('Kidney Disease', "Kidney Disease"),
            ('Tuberculosis', "Tuberculosis"),
            ('Asthma', "Asthma"),
            ('COPD', "COPD"),
            ('Diabetes', "Diabetes"),
            ('None of Above', "None of Above")
           
        ),
        widget = forms.CheckboxSelectMultiple,
       
    )

    symptoms = forms.MultipleChoiceField(label="Do you Have any of the following Symptoms",
        choices = (
            ('Loss of test or Smell', "Loss of test or Smell"), 
            ('Body Pain', 'Body Pain'),
            ('Fever', 'Fever'),
            ('Throat Pain', 'Throat Pain'),
            ('Weakness', 'Weakness'),
            ('Cough', 'Cough'),
            ('Diarrhoea', 'Diarrhoea'),
            ('Skin Rash', 'Skin Rash'),
            ('Breathlessness', 'Breathlessness'),
            ('None of Above', 'None of Above')
          ),
       
        widget = forms.CheckboxSelectMultiple,
        )

class PRegistrationForm(forms.Form):
    usernm=forms.CharField(widget=forms.TextInput(attrs={'title': 'Type your Username','placeholder': 'Your Usename'}),error_messages = {"key": "USername here..."},label="Username",max_length=50,min_length=4,empty_value=False,required=True)
    PR_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    PR_firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient First Name'}),label='Firstname',max_length=50,min_length=5,empty_value=False,required=True)
    PR_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient Last Name'}),label='Lastname',max_length=50,min_length=5,empty_value=False,required=True)
    PR_dob=forms.CharField(label="DOB",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)    
    sex=forms.ChoiceField(label="Gender",choices= GENDERS,required=True)
    PR_mobile=forms.CharField(label="Patient Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    PR_address=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter Patient postal address",'placeholder': "Address"}),label="Address",max_length=100,min_length=8,empty_value=False,required=True) 
    PR_photo=forms.ImageField(allow_empty_file=True,label="Patient photo",help_text='accept JPG/PNG file,max size 60 kb',required=False)
    
'''
class PrecForm(forms.Form):
    username=forms.ChoiceField(label="UserName",choices=GENDERS,required=True)
    pName=forms.CharField(label="Patient Name",max_length=50,min_length=4,empty_value=False,required=True)
    P_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient Last Name'}),label='Lastname',max_length=50,min_length=5,empty_value=False,required=True)
    sex=forms.ChoiceField(label="Gender",choices= GENDERS,required=True)
    age=forms.CharField(label="DOB",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)    
    prec=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5,'style':'height:7.5em;'}),label='Precription',max_length=200,min_length=4,empty_value=False,required=True)
'''