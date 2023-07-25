from django.urls import path
from loginpatient import views
urlpatterns = [
    path('login', views.login_page,name='login'),
    path('register', views.register,name='register'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('appointment', views.appointment,name='appointment'),
    path('covid', views.covid,name='covid'),
    path('history', views.history,name='history'),
    path('deletehistory/<int:id>/', views.delete_history, name="deletehistory"),
    path('logout', views.web_logout,name='logout'),
    path('changepassword', views.change_pass,name='changepassword'),
    path('registration', views.admin_Pregister, name="admin_Pregister"),
    path('userprescription', views.user_prescription, name="userprescription"),
    
    path('appointable', views.appoint_table, name="app_table"),
    path('covidtable', views.covid_table, name="covid_table"),
    path('delete', views.delete_data, name="deletedata"),
    path('deleteregister/<int:id>/', views.delete_register, name="deleteregister"),
    path('deletecovid', views.delete_covid, name="deletecovid"),
    path('export_appoint',views.export_appointments_xls,name='export_appointment'),
    path('export_prec',views.export_prescription_xls,name='export_prec'),
    path('export_covid',views.export_covid_xls,name='export_covid'),

]
