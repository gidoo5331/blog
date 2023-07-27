"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from .views import react
from .views import react
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$", react),
    re_path(r"^(?!admin)(?!api)(?!summernote)(?!auth)(?!api-auth)(?:.*)/?$", react),

    # Django summer note
    path('summernote/', include('django_summernote.urls')),
    
    # url paths for each app's url
    path('api/blog/' , include('blog.urls')),
    path('api/', include('navbarFooter.urls')),
    # path('', include('accounts.urls')),

    # Djoser
    path('auth/', include('djoser.urls')),
    # Djoser with JSON WEB TOKEN URLS
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),

    # restFrameWork urls
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)