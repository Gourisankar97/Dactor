from django.urls import path
from . import views

urlpatterns = [
    path('fix_appointment', views.fix_appointment, name='fix_appointment'),
    path('myappointments', views.myappointments, name='myappointments'),
    path('dr_login', views.dr_login, name='dr_login'),
    path('search', views.search, name='search'),
    path('feedback', views.feedback, name='feedback'),
    path('cancel_appointment', views.cancel_appointment, name='cancel_appointment'),
    path('Account_Info', views.Account_Info, name='Account_Info'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('Update_Account_Info', views.Update_Account_Info, name='Update_Account_Info'),
    path('Update_password', views.Update_password, name='Update_password'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('new_password', views.new_password, name='new_password'),
    path('Dactor', views.Dactor, name='Dactor')
    



]