from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('Appointment', views.Appointment, name='Appointment'),
    path('cancelapp', views.cancelapp, name='cancelapp'),
    
    path('my_appointments', views.my_appointments, name='my_appointments'),



]