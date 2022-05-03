from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, user_name, email, first_name, last_name, password, **other_fields ):
        if not email:
            raise ValueError('Please enter your email')
        if not user_name:
            raise ValueError('Enter user_name')
         
        user = self.model(
            email= self.normalize_email(email),
            user_name= user_name, first_name= first_name, 
            last_name= last_name, password= password, **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, user_name, email, first_name, last_name, password, **other_fields, ):
        
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get ('is_staff') is not True:
            raise ValueError('Superusers must be assigned to is_staff=True.')
        
        if not email:
            raise ValueError('Please enter your email')
        if not user_name:
            raise ValueError('Enter user_name')
            
        user = self.create_user(
            email= self.normalize_email(email),
            user_name= user_name, first_name= first_name, 
            last_name= last_name, password= password, **other_fields,
        )

        # user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    user_name       =models.CharField(max_length=70, unique=True)
    email           =models.EmailField(max_length=150, unique=True)
    first_name      =models.CharField(max_length=60,)
    last_name       =models.CharField(max_length=60)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_admin        =models.BooleanField(default=False)
    date_joined     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(default=timezone.now)

    objects = MyUserManager()


    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name
