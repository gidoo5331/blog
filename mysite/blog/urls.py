from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
path('m', TemplateView.as_view(template_name="blog/index.html")),
path('', PostList.as_view(), name='listcreate'),
path('category', CatergoryView.as_view(), name='category-list'),
path('featured', FeaturedPost.as_view(), name='featured'),
path('post/<slug:slug>/', DetailedView.as_view(), name='detailedPost'),
] 