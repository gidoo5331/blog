from imp import source_from_cache
from unicodedata import category
from rest_framework import serializers
from .models import Post

# class PostSerializer(serializers.HyperlinkedModelSerializer):
class PostSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source= 'category.name')
    category = serializers.CharField(source= 'category.name')
    created_by = serializers.CharField(source= 'created_by.first_name')
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        # fields = ['id', 'title', 'content', 'exceprt', 'image', 'featured', 'category_name', 'created_by',]
       
        # for Slug
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }