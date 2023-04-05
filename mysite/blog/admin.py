from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

# class PostAdmin(SummernoteModelAdmin):


# Register your models here.
# class PostAdmin(admin.ModelAdmin, SummernoteModelAdmin):
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)