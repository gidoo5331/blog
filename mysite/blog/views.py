from rest_framework import generics
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser ,IsAuthenticatedOrReadOnly,IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.
# Blog_api
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    try:
        # queryset = Post.objects.select_related('created_by','category').all()
        queryset = Post.objects.all()
   
    except:
        queryset = Post.objects.all()

    serializer_class = PostSerializer
    # pass

class FeaturedPost(generics.ListAPIView):
    queryset = Post.objects.all().filter(featured=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny, ]

  
# Category Data
class CatergoryView(generics.ListAPIView):
    queryset = Post.objects.all()
    # print(queryset)
    permission_classes = [AllowAny,]
    serializer_class =PostSerializer
    # Using query_params
    def get(self, request, format=None):
        # Get Query Param from get request
        data = self.request.query_params

        # get category from query param obj
        category_obj = data.get('category')

        # Get post from db, filter using category_obj
        queryset = Post.objects.filter(category__slug = category_obj)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

# Detailed View
class DetailedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug) 
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, slug, format=None):
        serializer_context = {
            'request': request,
        }
        post = self.get_object(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)