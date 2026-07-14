from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        (1, 'SuperAdmin'),
        (2, 'Admin'),
        (3, 'User'),
    )


    firstname = models.CharField(max_length=100,null=True, blank=True)
    lastname = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPES, null=True, blank=True)
    password = models.CharField(max_length=100,null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=False)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):   
        return self.email