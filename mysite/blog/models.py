# from msilib.schema import Environment
# from unicodedata import category
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import MyUser

class Category(models.Model):
    name            =models.CharField(max_length=250, unique=True, default='World')
    slug            =models.SlugField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title               =models.CharField(max_length=100)
    category            =models.ForeignKey(Category, related_name='post' ,on_delete=models.CASCADE)
    created_by          =models.ForeignKey(MyUser, related_name='content_creator', on_delete=models.CASCADE)
    exceprt             =models.CharField(null=True, max_length=150)
    image               =models.ImageField(upload_to="images/", default='images/default.jpg')
    content             =models.TextField(null=True)
    featured            =models.BooleanField(default=False)
    slug                =models.SlugField(null=False, max_length=250, unique=True)
    is_active           =models.BooleanField(default=False)
    created             =models.DateTimeField(auto_now_add=True)
    updated             =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title