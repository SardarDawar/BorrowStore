from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from .models import infor,staff_contractor
import random
from django.forms.models import model_to_dict
from .forms import staff_contractor_form

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    template = 'login.html'
    if request.method == 'POST':
        a = authenticate(username=request.POST['uname'],password=request.POST['password'])
        if a is not None:
            auth.login(request,a)
            return redirect('/')
    return render(request,template,{'formnum':1})

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    template = 'login.html'
    form = staff_contractor_form(request.POST)
    if request.method == 'POST' and form.is_valid():
        sc = form.cleaned_data
        un = request.POST['uname']
        pas = request.POST['password']
        objs = User.objects.all()
        for i in objs:
            if i.username == un:
                return redirect('/')
        a = User.objects.create_user(
            un,
            request.POST['email'],
            pas
        )
        a.last_name = request.POST['lname']
        a.first_name = request.POST['fname']
        a.save()
        i = infor.objects.get(user=a)
        i.passwordkey = randomizer()
        i.save()
        obj = staff_contractor(
            staff_name = sc['staff_name'],
            phone_password = sc['phone_password'],
            job_title = sc['job_title'],
            work_phone = sc['work_phone'],
            home_phone = sc['home_phone'],
            mobile_phone = sc['mobile_phone'],
            fax_number = sc['fax_number'],
            address_line_1 = sc['address_line_1'],
            address_line_2 = sc['address_line_2'],
            city = sc['city'],
            province_state = sc['province_state'],
            postal_code_ZIP = sc['postal_code_ZIP'],
            country_region = sc['country_region'],
            web_page = sc['web_page'],
            notes = sc['notes'],
            user = a,    
        )    
        obj.save()
        return redirect('/login')
    else:
        form = staff_contractor_form()
    return render(request,template,{'formnum':2,'form':form})

def reset1(request):
    template = 'login.html'
    context = {'formnum':3}
    if request.method == 'POST':
        a = request.POST['uname']
        objs = User.objects.all()
        for i in objs:
            if a == i.username or a == i.email:
                message = EmailMessage(
                    subject='Reset your password',
                    body='Go to the following link : \n https://127.0.0.1:8000/new-password/'+(infor.objects.get(user=i).passwordkey),
                    to=[i.email]
                )
                message.send()
                return redirect('/login')
    return render(request,template,context)

def reset2(request,key):
    template = 'login.html'
    context = {'formnum':4}
    obj = infor.objects.get(passwordkey = key)
    users = User.objects.all()
    for i in users:
        if i == obj.user:
            userobj = i
    if request.method == 'POST':
        a = request.POST['password']
        b = request.POST['password1']
        if a == b:
            userobj.set_password(a)
            userobj.save()
            auth.login(request,authenticate(username = userobj.username,password = a))
            return redirect('/')
        else:
            return redirect('/new-password/'+obj.passwordkey)
    return render(request,template,context)

def editpro(request):
    template = 'login.html'
    context = {'formnum':5}
    obj = staff_contractor.objects.get(user=request.user)
    context['obj'] = obj
    if request.method == 'POST':
        sc = request.POST
        obj.staff_name = sc['staff_name']
        obj.phone_password = sc['phone_password']
        obj.job_title = sc['job_title']
        obj.work_phone = sc['work_phone']
        obj.home_phone = sc['home_phone']
        obj.mobile_phone = sc['mobile_phone']
        obj.fax_number = sc['fax_number']
        obj.address_line_1 = sc['address_line_1']
        obj.address_line_2 = sc['address_line_2']
        obj.city = sc['city']
        obj.province_state = sc['province_state']
        obj.postal_code_ZIP = sc['postal_code_ZIP']
        obj.country_region = sc['country_region']
        obj.web_page = sc['web_page']
        obj.notes = sc['notes']
        obj.save()
        obj = staff_contractor.objects.get(user=request.user)
        context['obj'] = obj
    return render(request,template,context)

def randomizer():
    a = 'abcdefghijklmnopqrstuvwxyz1234567890'
    c = ''
    for i in range(0,25):
        c = c + a[random.randint(0,len(a)-1)]
    return c