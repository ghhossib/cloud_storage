from symtable import Class

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


#создание своей модели User
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    object = UserManager()

    def save(self,*args,**kwargs):
        if self.password and not self.password.startswitch('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.email


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extar_filds):
        if not email:
            raise ValueError('Вы не ввели свой Email')
        user = self.normalize_email(email)
        user = self.model(email, **extar_filds)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_filds):

        extra_filds.setdefault('is_staff',True)
        extra_filds.setdefault('is_superuser',True)
        extra_filds.setdefault('is_active',True)
        if extra_filds.get('is_staff') is not True:
            raise ValueError("Суперпользователь должен is staff = True")
        if extra_filds.get('is_superuser') is not True:
            raise ValueError("Суперпользователь должен is superuser = True")
        return self.create_user(email,password,**extra_filds)
