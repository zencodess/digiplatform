from django.db import models
from typing import Set
from django. core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MemberManager(BaseUserManager):
    use_in_migrations = True
        
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email should be set')
        if not password:
            raise ValueError('Password should be set')
        email = self.normalize_email(email)
        user_info = self.model(email=email, **extra_fields)
        user_info.set_password(password)
        user_info.save(using=self._db)
        return user_info

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, **extra_fields)
        
    def create_accountmanager(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser should be a superuser.')

        return self._create_user(email, password, **extra_fields)
        


class AccountManager(AbstractBaseUser, PermissionsMixin, MemberManager):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(unique=True) # by default each feild is required
    date_joined = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    object = MemberManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email   
    
    def createcustomer(self, email, password, **extra_fields):
        # email, password, name, date_joined, is_active='', is_admin=False, is_staff=False
        Customer.objects.get_or_create(email, password, **extra_fields)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(AccountManager, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=128, unique=True)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    def serve(self):
        return 'SUCCESS'
        
        
class Customer(models.Model):
    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        
    username = None
    email = models.EmailField('email', unique=True)
    name = models.CharField(max_length=30, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name']
    
    account_manager = models.ForeignKey(
                            AccountManager,
                            on_delete=models.PROTECT,
            )
    
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def email(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
    def __str__(self):
        return self.email
        
    def has_perm(self):
        return self.is_admin
        
    order = models.ManyToManyField(
                    Service,
                    through="Ordering",
                    through_fields=("customer", "service"),
                )
                        
   
class Ordering(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)