from django.urls import path
from .views import  NavbarView, FooterView, FooterCssView

urlpatterns = [
    path('navbar/', NavbarView.as_view(), name='navbar'),
    path('footer/', FooterView.as_view(), name='footer'),
    path('footer/css', FooterCssView.as_view(), name='footer'),
]