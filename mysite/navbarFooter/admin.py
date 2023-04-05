from django.contrib import admin
from .models import Navbar, Footer, SocialMediaIcon, FooterCss

# Register your models here.
class NavbarAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('navbrandName', 'navbrandImage',)}),
        ('Links', {'fields': ('link1', 'link2', 'link3', 'link4', 'link5', 'alt5', 'link6', 'alt6',)}),
        ('Navbar Css', {'fields': ('navbarTextColor', 'navbarBackgroundColor', 'navbarHoverTextColor', )}),

    )
admin.site.register(Navbar, NavbarAdmin)


class FooterAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('title',)}),
        ('Column1', {'fields': ('row1', 'row2', 'row3', 'row4', 'row5', 'row6',)}),
        # ('Permissions', {'fields': ('in_stock', 'is_active', )}),
    )
admin.site.register(Footer, FooterAdmin)

# Footer css
class FooterCssAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('title',)}),
        ('Footer Css', {'fields': ('footerTextColor', 'footerBackgroundColor', 'footerBackgroundImage',)}),
    )

admin.site.register(FooterCss, FooterCssAdmin)


class SocialMediaIconAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('name', 'icon', 'link')}),
    )

admin.site.register(SocialMediaIcon, SocialMediaIconAdmin)