from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .lib import *


# Create your views here.
def home(request):
  if request.user.is_authenticated:
    return redirect(find_worker)
  return render(request,'index.html')
  
def find_worker(request):
  
  
  workers = Worker.objects.all()
  
  for i in workers:
    print(i.avatar.url)
  
  return render(request,'findworker.html',{'workers': workers})
  
def login_user(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if not User.objects.filter(email=email).exists():
      messages.info(request,'email does not exists')
      return redirect(login_user)
    
    user = User.objects.get(email=email)
    
    print(password)
    
    if check_password(password,user.password):
      print('True')
    else:
      print('False')
    
    if not user.check_password(password):
      print('password did not match')
      messages.info(request,'password did not match')
      return redirect(login_user)
    
    uid = authenticate(email=email,password=password)
    login(request,uid)
    
    return redirect(home)
    
  return render(request,'login.html')

def works(request):
  return render(request,'works.html')


def signup(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')
    
    if not User.objects.filter(email=email).exists():
      messages.info(request,'Email already exist')
      print("already exists")
      redirect(signup)
      
    
    if not password == password1:
      messages.info(request,'Password didnt match')
      print('password didnt match')
      redirect(signup)
     
    
    user = User.objects.create_user(email=email,password=password1)
    
    uid = authenticate(email=email, password=password)
    login(request,uid)
    
    return redirect(home)
    
    
  return render(request,'signup.html')

def be_a_worker(request):
  return render(request,'became_a_worker.html')


def worker_signup(request):
  if not request.user.is_authenticated:
    return redirect(login_user)
    
  if request.method == 'POST':
    name = request.POST.get('name')
    district = request.POST.get('district')
    phone_no = request.POST.get('phone_no')
    city = request.POST.get('city')
    street_address = request.POST.get('street_address')
    pin = request.POST.get('pin')
    job_title = request.POST.get('job_title')
    experience = request.POST.get('experience')
    avatar = request.FILES.get('avatar')
    resume = request.FILES.get('resume')
    notification = request.POST.get('notification')
    notification = bool(notification)
    Worker.objects.create(name=name,district=district,phone_no=phone_no,city=city,street_address=street_address,pin=pin,job_title=job_title,experience=experience,avatar=avatar,resume=resume,user_id=request.user,notification=notification)
    user = User.objects.get(pk=request.user.id)
    user.is_worker = True
    user.save()
    
    messages.info(request,'Worker registration successfull')
    return redirect(home)
  
  
  return render(request,'worker_signupform.html',{'district':district_list})
  
def logout_user(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect(home)
  return redirect(login_user)