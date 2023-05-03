from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username address')
        if not password:
            raise ValueError('Users must have a password')
        username = self.normalize_email(username)
        username = username.lower()
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username address')
        if not password:
            raise ValueError('Users must have a password')
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(max_length=254, unique=True)
    balance = models.IntegerField(default=20)
    #
    is_staff = models.BooleanField(default=False)
    #
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self) -> str:
        return self.username
