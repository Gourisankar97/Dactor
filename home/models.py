from django.db import models
#from phone_field import PhoneField

# Create your models here.


class Dr_Registration(models.Model):

    Dr_name = models.CharField(max_length=50)
    Dr_email_id = models.CharField(max_length=50)
    Dr_phone_no = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    Dr_photo = models.ImageField(upload_to='pics')
    Dr_city = models.CharField(max_length=20)
    Dr_specialization = models.CharField(max_length=30)
    Dr_address = models.CharField(max_length=200)
    Dr_Details = models.CharField(max_length=200)
    Dr_timeings = models.TimeField()

class Appointments(models.Model):
    Dr_name = models.CharField(max_length=50)
    Dr_Adress = models.CharField(max_length=200)
    Dr_specialization = models.CharField(max_length=30)
    Dr_timeings = models.TimeField()
    Patient_name = models.CharField(max_length=50)
    Appt_Date = models.DateField()
    user_id = models.CharField(max_length=10)

class Or_Appointments(models.Model):
    Dr_name = models.CharField(max_length=50)
    Dr_Adress = models.CharField(max_length=200)
    Dr_specialization = models.CharField(max_length=30)
    Dr_timeings = models.TimeField()
    Patient_name = models.CharField(max_length=50)
    Appt_Date = models.DateField()
    user_id = models.CharField(max_length=10)





