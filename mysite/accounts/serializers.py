from rest_framework import serializers
from .models import *

# DJOSER
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# DJOSER SECTION
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields  = ['email', 'user_name', 'first_name', 'last_name', 'password']



# class RegisterUserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model   = MyUser
#         fields  = ['email', 'user_name', 'first_name', 'last_name', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     # for authentication
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
 