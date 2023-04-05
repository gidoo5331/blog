from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import NavbarSerializer, FooterSerializer, SocialMediaIconSerializer,FooterCssSerializer 
from .models import Navbar, Footer, SocialMediaIcon, FooterCss

# NavbarView
class NavbarView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset    =Navbar.objects.all()
    serializer_class    = NavbarSerializer

# FooterView
class FooterView(ListAPIView):
    permission_classes = [AllowAny]
    queryset    =Footer.objects.all()
    serializer_class    = FooterSerializer


# SocialMediaIconView
class SocialMediaIconView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset    =SocialMediaIcon.objects.all()
    serializer_class    = SocialMediaIconSerializer

# FooterCssView
class FooterCssView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset    =FooterCss.objects.all()
    serializer_class    = FooterCssSerializer