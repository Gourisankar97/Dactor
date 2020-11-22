from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Dr_Registration, Appointments
from django.contrib import sessions


# Create your views here.


def index(request):
    return render(request, 'Home.html')


def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    Email = request.POST['email']
    user_name = request.POST['user_name']
    password = request.POST['pwd']
    print('Working')
    if User.objects.filter(username=user_name).exists():
        um = 'Usename already taken!'
        return render(request, 'Home.html',{'username_taken':um})
    elif User.objects.filter(email=Email).exists():
        em = 'Email already Registered!'
        return render(request, 'Home.html', {'email_taken':em})
    else:
        user = User.objects.create_user(username=user_name, password=password, first_name=first_name, last_name=last_name, email=Email)
        user.save()
        # import smtplib
        # from email.mime.multipart import MIMEMultipart
        # from email.mime.text import MIMEText
        # Company_mail = 'gourisankar941@gmail.com'
        # receiver_mail = Email
        # messages = "Welcome! \nHi {}, welcome to Dactor. Now you can consult to your local doctors anywhere anytime.... ".format(first_name)
        # subject = 'Welcome To Dactor.in'
        # sms = MIMEMultipart()
        # sms['From'] = Company_mail
        # sms['To'] = receiver_mail
        # sms['subject'] = subject
        # sms.attach(MIMEText(messages,'plain'))
        # text = sms.as_string()
        # server = smtplib.SMTP('smtp.gmail.com',587)
        # server.starttls()
        # server.login(Company_mail,'tapu12345')
        # server.sendmail(Company_mail,receiver_mail,text)
        # server.quit()
        msg = 'you have successfully registed! login for more !'
        return render(request, 'Home.html', {'msg':msg})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['lpwd']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
                # request.sessions['id'] = User.objects.only('id')
            return redirect('Dactor')

            # drs = Dr_Registration.objects.all()

            # return render(request, 'FindDoctor.html', {'dr_details': drs})
        else:
            error = 'inavalid username or password'
            return render(request, 'Home.html', {'error_msg':error} )
    else:
        return render(request,'Home.html')


def Appointment(request):
    if request.user.is_authenticated:

        id = request.GET['drid']
        my_id = request.user.id

        # request.sessions['drid'] = id

        quory = Dr_Registration.objects.filter(id=id).only('Dr_name', 'Dr_specialization', 'Dr_address', 'Dr_timeings', 'Dr_Details', 'Dr_photo', 'Dr_phone_no', 'id')

        return render(request, 'Appointment.html', {'dr_details': quory, 'my_id': my_id})
    else:
        return render(request, 'Home.html')

def cancelapp(request):
    return render(request, 'cancellation.html')

def my_appointments(request):
    if request.user.is_authenticated:

        user = request.user
        my_id = user.id
        my_appoints = Appointments.objects.filter(id=my_id).all()  


        return render(request, 'my_appointments.html')
    else:
        return render(request, 'Home.html')





