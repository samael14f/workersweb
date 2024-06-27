import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not specified a valid e-mail address")
    
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
            
class Worker(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='uploads/avatars')
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street_address = models.TextField()
    pin = models.CharField(max_length=6)
    phone_no = models.CharField(max_length=15)
    experience = models.IntegerField()
    job_title = models.CharField(max_length=255)
    resume = models.FileField(upload_to="uploads/resume")
    notification = models.BooleanField(default=False)
    is_available= models.BooleanField(default=True)
    
    def __str__(self):
      return self.name
    
    
    
class Work(models.Model):
    name = models.CharField(max_length=255)
    work_by = models.ForeignKey(User,on_delete= models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True)
    is_cancelled = models.BooleanField(default=False)
    def __str__(self):
      return self.name
     
    
class UserAddress(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)
    adrress = models.TextField()
    district = models.CharField(max_length=255)
    pin = models.CharField(max_length=6)
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class WorkRequest(models.Model):
  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    
    