
from django.urls import path, include

from .views import *


urlpatterns = [
  
  path('',home,name="home"),
  path('find_worker/',find_worker,name="find_worker"),
  path('login/',login_user,name='login'),
  path('works/',works,name="works"),
  path('be-a-worker/',be_a_worker,name="be-a-worker"),
  path('worker-signup/',worker_signup,name="worker-signup"),
  path('signup/',signup,name="signup"),
  path('logout/',logout_user,name='logout'),
  path('worker/<int:pk>',worker,name='worker'),
  path('work-request/<int:pk>', request_work,name='request_work'),
  path('work-notifications/',work_notifications,name="work-notifications"),
  path('work-notifications/work-authorizer/<int:pk>',work_authorizer,name="work-authorizer"),
  ] 