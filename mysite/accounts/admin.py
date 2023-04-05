from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display    = ('user_name', 'email', 'first_name', 'last_name')
    list_filter     = ('first_name', 'is_admin')
    fieldsets       =(
        (None, {'fields': ('user_name', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissons', {'fields': ('is_active', 'is_admin', 'is_staff')}),
    )
    add_fieldsets =(
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff',)}),
    )
    
    search_fields = ('user_name',)
    ordering = ('user_name',)
    filter_horizontal = ()

admin.site.register(MyUser, CustomUserAdmin)