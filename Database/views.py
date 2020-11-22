from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Appointments, Feedbacks
from home.models import Dr_Registration
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
# Create your views here.

def fix_appointment(request):
    if request.user.is_authenticated:
        my_id = request.user.id
        if request.method == 'POST':
            Dr_id = request.POST['fix']
            my_id = request.POST['My_id']
            patient_name = request.POST['pname']
            Appt_date = request.POST['mydate']

        # fetching dr. details
            Drs_Details = Dr_Registration.objects.filter(id=Dr_id).all()

            for Drs in Drs_Details:

                Dr_name = Drs.Dr_name
                Dr_spec = Drs.Dr_specialization
                Dr_address = Drs.Dr_address
                Dr_time = Drs.Dr_timeings


        # Storing about the appointment
            appoint = Appointments.objects.create(Dr_name=Dr_name, Dr_Adress=Dr_address, Dr_specialization=Dr_spec, Dr_timeings=Dr_time, Patient_name=patient_name, Appt_Date=Appt_date, user_id=my_id)
            appoint.save()
            
            return render("success_appt.html", {'my_id': my_id})
        else:
            return render("success_appt.html",{'my_id': my_id})
    else:
        return redirect('index')


def myappointments(request):
    if request.user.is_authenticated:
        user = request.user
        my_id = user.id
        myapps_count = 0

        myapps = Appointments.objects.filter(user_id=my_id)
        myapps_count = Appointments.objects.filter(user_id=my_id).count()
        if(myapps_count==0):
            message = "No record found"
            return render(request, 'my_appointments.html',{'message': message})

        return render(request, 'my_appointments.html', {'myapps': myapps})
    else:
        return redirect('index')

def dr_login(request):
    dr_email = request.POST['dr_email']
    dr_pwd = request.POST['dr_pwd']
    try:

        Dr_auth = Dr_Registration.objects.filter(Dr_email_id=dr_email,password=dr_pwd).get()
        if Dr_auth is not None:
            Dr_name = Dr_auth.Dr_name

            Drs_Appointments = Appointments.objects.filter(Dr_name=Dr_name).all()
            return render(request,'Dr_Panel.html', {'Drs':Drs_Appointments})
    except:
        return render(request,'Home.html')

def search(request):
    if request.user.is_authenticated:

        city = request.GET['city']
        dr_spec = request.GET['dr_specialization']
        dr_details = 0
        messages = "No Doctors Available"
        if(city == '0' and dr_spec != '0'):
            try:

                dr_details = Dr_Registration.objects.filter(Dr_specialization=dr_spec).all()
                dr_count = Dr_Registration.objects.filter(Dr_specialization=dr_spec).count()
                if(dr_count==0):
                    return render(request,'FindDoctor.html', {'message':messages})
                    
                return render(request,'FindDoctor.html', {'dr_details':dr_details})
            except:
                messages = "No Doctors Available"
                return render(request,'FindDoctor.html', {'message':messages})
        if(city != '0' and dr_spec == '0'):

            try:

                dr_details = Dr_Registration.objects.filter(Dr_city=city).all()
                dr_count = Dr_Registration.objects.filter(Dr_city=city).count()
                if(dr_count==0):
                    return render(request,'FindDoctor.html', {'message':messages})
            
                return render(request,'FindDoctor.html', {'dr_details':dr_details})
            except:

                messages = "No Doctors Available"
                return render(request,'FindDoctor.html', {'message':messages}) 
        if(city != '0' and dr_spec != '0'):
            try:
                dr_details = Dr_Registration.objects.filter(Dr_city=city,Dr_specialization=dr_spec).all()
                dr_count = Dr_Registration.objects.filter(Dr_city=city,Dr_specialization=dr_spec).count()
                if(dr_count==0):
                    return render(request,'FindDoctor.html', {'message':messages})
            
                return render(request,'FindDoctor.html', {'dr_details':dr_details})
            except:

                messages = "No Doctors Available"
                return render(request,'FindDoctor.html', {'message':messages})
    else:
        return redirect('index')

    
def feedback(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        feedback = request.POST['feedback']

        save_feed = Feedbacks.objects.create(Name=Name,Email=Email,Message=feedback)
        save_feed.save()
        return HttpResponse('')


def cancel_appointment(request):
    if request.user.is_authenticated:
        cnclapptid = request.GET['cnclapptid']
        Appointments.objects.filter(id=cnclapptid).delete()
        user = request.user
        my_id = user.id

        myapps = Appointments.objects.filter(user_id=my_id)
    else:
        return redirect('index')

    return render(request, 'my_appointments.html', {'myapps': myapps})
def Account_Info(request):
    if request.user.is_authenticated:
        user = request.user
        return render( request,'AccountInfo.html', {'user':user})
    else:
        return redirect('index')
    
def Update_Account_Info(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            fn = request.POST['fn']
            ln = request.POST['ln']
            em = request.POST['em']
            user = request.user
            userid = user.id
            upadate = User.objects.get(id=userid)
            upadate.first_name=fn
            upadate.last_name=ln
            upadate.email=em
            upadate.save()
            user = User.objects.get(id=userid)
            return render(request, 'AccountInfo.html',{'user':user} )
    else:
        return redirect('index')
def Dactor(request):
    if request.user.is_authenticated:
        
        drs = Dr_Registration.objects.all() 
        page = request.GET.get('page', 1)
        paginator = Paginator(drs,12)
        try:
            doctors = paginator.page(page)
        except PageNotAnInteger:
            doctors = paginator.page(1)
        except EmptyPage:
            doctors = paginator.page(paginator.num_pages)

        return render(request, 'FindDoctor.html', {'dr_details': doctors})




def changepassword(request):
    if request.user.is_authenticated:
        return render(request, 'changepassword.html')

def Update_password(request):
    if request.user.is_authenticated:
        user = request.user
        userid = user.id
        # c=0
        if request.method == 'POST':
            # current_pwd = request.POST['cpwd']
            Con_pwd = request.POST['ncpwd']
            u = User.objects.get(id=userid)
            u.set_password(Con_pwd)
            u.save()
            u = User.objects.get(id=userid)
            message = "password changed succesfully!"
            return render(request, 'AccountInfo.html',{'user':user, 'message':message})
        else:
            
            return render(request, 'changepassword.html')
    else:
        return redirect('index')

def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')
    else:
        
        return render(request, 'Home.html')

def forgot_password(request):
    if request.method == 'POST':
        uname = request.POST['un']
        email = request.POST['em']
        c=0
        c = User.objects.filter(username=uname,email=email).count()
        if(c!=0):
            return render(request,'cp.html',{'uname':uname})
        else:
            msg = 'invalid username or email'
            return render(request, 'forgotpassword.html',{'msg':msg})
    return render(request,'forgotpassword.html')

def new_password(request):
    if request.method == 'POST':
        newpassword = request.POST['ncpwd']
        uname = request.POST['uname']
        u = User.objects.get(username=uname)
        u.set_password(newpassword)
        u.save()
        return render(request,'Home.html')
    else:
        return redirect('index')






