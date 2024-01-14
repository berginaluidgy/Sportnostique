
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from datetime import date 


class CustomUserManager(UserManager):
    def _create_user(self, name, password, **extra_fields):
        
        
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)
    
    def create_superuser(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=True, default='', unique=True ,max_length=255)
    prenom=models.CharField(max_length=255 )  
    password=models.CharField(max_length=255)
    username=None
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    
# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser) :
    
#     name=models.CharField(max_length=255,unique=True)
#     prenom=models.CharField(max_length=255)  
#     password=models.CharField(max_length=255)
#     username=None
#     USERNAME_FIELD='name'
#     REQUIRED_FIELDS=[]
    
# from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager): 
#     def create_user(self, username, password = None, **extra_fields): 
#         user = self.model(username=username, **extra_fields)

#         user.set_password(password)
#         user.save(using = self.db)
#         return user

#     def create_superuser(self, username='Bergina', password = None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         return self.create_user(username, password, **extra_fields)    





class Account(models.Model):
    nom=models.CharField(max_length=90)
    prenom=models.CharField(max_length=90)
    tel=models.IntegerField(max_length=15)
    affiliate=models.IntegerField(max_length=10)
    argentGagner=models.IntegerField(max_length=10)
    codeAff=models.IntegerField(max_length=10)
    identifiant=models.IntegerField(max_length=10)
    date=models.DateField(default=date.today)
    actifaccount=models.BooleanField(default=False)
    def get_full_name(self):
        return self.nom
    
class SuperAdmin(models.Model):
    nom=models.CharField(max_length=20)  
    prenom=models.CharField(max_length=20)
    nbrOfUser=models.IntegerField(max_length=10) 
    Gain=models.IntegerField(max_length=20) 
    nbrUsergain=models.IntegerField(max_length=20)
    


class plan(models.Model):
    nom=models.CharField(max_length=255)    
    active=models.BooleanField(default=False)
    datepayment=models.DateField(default=date.today)
    # dateexpire=models.DateField(default=)
  