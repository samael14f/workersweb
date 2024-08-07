from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .lib import *
from datetime import date

# Create your views here.
def home(request):
  if request.user.is_authenticated:
    return redirect(find_worker)
  return render(request,'index.html')
  
def find_worker(request):
  
  if request.method == "POST":
    search_key = request.POST.get('search_key')
    district = request.POST.get('district')
    print(search_key,district)
    if not district:
      workers = Worker.objects.filter(name__contains=search_key)
    workers = Worker.objects.filter(name__contains,district=district)
    if not workers:
      print('kskd')
      workers = Worker.objects.filter(job_title__contains=search_key)
  elif request.method == "GET":
    workers = Worker.objects.all()
  
  for i in workers:
    print(i.avatar.url)
  
  return render(request,'findworker.html',{'workers': workers,'districts':district_list})
  
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
  works = Work.objects.all()
  return render(request,'works.html',{'works':works})

def jobs(request):
  works = Work.objects.all()
  return render(request,'job.html',{"works":works})

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
  
  
def worker(request,pk):
  
  if request.user.is_authenticated:
    worker = Worker.objects.get(pk=pk)
    review = Review.objects.filter(worker=worker)
    
    return render(request,'worker.html',{'worker':worker, 'reviews':review})
  return redirect(login_user)
  
  
def request_work(request,pk):
  if not request.user.is_authenticated:
    return redirect(login_user)
    
  worker = Worker.objects.get(pk=pk)
  if request.method == 'POST':
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    date = request.POST.get('date')
    
    print(name,desc,date)
    
    WorkRequest.objects.create(user=request.user,name=name,desc=desc,date=date,worker=worker)
    
    
  
  return render(request,'request_work.html',{'worker':worker})
  

def work_notifications(request):
  if not request.user.is_authenticated:
    return redirect(login_user)

  today = date.today()
  print(today)
  work_request = WorkRequest.objects.all()
    
  return render(request,'work_notification.html',{'work_requests':work_request,"today":today})
  
  
def work_authorizer(request,pk):
  if request.method == "POST":
    work_request = WorkRequest.objects.get()
    is_accepted = bool(int(request.POST.get('a_btn')))
    work_request.is_accepted = is_accepted
    work_request.save()
    
    Work.objects.create(name=work_request.name,desc=work_request.desc,work_by=work_request.user,worker=work_request.worker,date=work_request.date)
    
  return redirect(work_notifications)


def profile(request):
  profile=None
  worker=None
  
  if Profile.objects.filter(user_id=request.user).exists():
    profile = Profile.objects.get(user_id=request.user)
  if Worker.objects.filter(user_id=request.user).exists():
    
    worker = Worker.objects.get(user_id=request.user)
    print("exists 1212")
  
  if request.method == 'POST':
    available = request.POST.get('available')
    worker = Worker.objects.get(user_id=request.user)
   
    worker.is_available = available == 'True'
    print('iikxk',type(available),available)
    worker.save()
    # worker.is_available =

  return render(request,'profile.html',{'Profile':profile,"worker":worker})
  
 
def add_profile(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    district = request.POST.get('district')
    phone_no = request.POST.get('phone_no')
    city = request.POST.get('city')
    street_address = request.POST.get('street_address')
    pin = request.POST.get('pin')
    avatar = request.FILES.get('avatar')
    Profile.objects.create(name=name,district=district,phone_no=phone_no,city=city,street_address=street_address,pin=pin,avatar=avatar,user_id=request.user)
    return redirect(profile)
    
  return render(request,'add_profile.html',{'district':district_list})
  
  
def work_or_job(request,pk):
  work = Work.objects.get(pk=pk)
  review = Review.objects.filter(work=work)
  if request.method == 'POST':
    is_completed = bool(int(request.POST.get('is_completed')))
    work.is_completed = is_completed
    work.save()
    return redirect(work_or_job,work.id)
  return render(request,'work_or_job.html',{"work":work,'reviews':review})
  
  
def add_review(request,work_id):
  if request.method == 'POST':
    body = request.POST.get('body')
    work = Work.objects.get(pk=work_id)
    print('user',work.work_by)
    print('worker',work.worker)
    Review.objects.create(user=work.work_by,body=body,worker=work.worker,work=work)
  return redirect(work_or_job,work_id)