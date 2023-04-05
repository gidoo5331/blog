from rest_framework import serializers
from .models import *

class NavbarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Navbar
        fields  = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Footer
        fields  = '__all__'

# footer css
class FooterCssSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = FooterCss
        fields  = '__all__'

class SocialMediaIconSerializer(serializers.ModelSerializer):

    class Meta:
        model   = SocialMediaIcon
        fields  = '__all__'
