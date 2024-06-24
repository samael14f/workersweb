from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'index.html')
  
def find_worker(request):
  return render(request,'findworker.html')
  
def login(request):
  return render(request,'login.html')

def works(request):
  return render(request,'works.html')


def signup(request):
  return render(request,'signup.html')

def be_a_worker(request):
  return render(request,'became_a_worker.html')


def worker_signup(request):
  return render(request,'worker_signupform.html')