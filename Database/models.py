from django.db import models

# Create your models here.


class Appointments(models.Model):

    Dr_name = models.CharField(max_length=50)
    Dr_Adress = models.CharField(max_length=200)
    Dr_specialization = models.CharField(max_length=30)
    Dr_timeings = models.TimeField()
    Patient_name = models.CharField(max_length=50)
    Appt_Date = models.DateField()
    user_id = models.CharField(max_length=10)


class Feedbacks(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Message = models.CharField(max_length=1000)
    