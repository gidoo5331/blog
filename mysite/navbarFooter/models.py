from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Navbar(models.Model):
    navbrandName        =models.CharField(max_length=40)
    navbrandImage       =models.ImageField(upload_to='images/')
    link1               =models.CharField(max_length=70, blank=True)
    link2               =models.CharField(max_length=70, blank=True)
    link3               =models.CharField(max_length=70, blank=True)
    link4               =models.CharField(max_length=70, blank=True)
    link5               =models.CharField(max_length=70, blank=True)
    alt5                =models.CharField(max_length=70, blank=True)
    link6               =models.CharField(max_length=70, blank=True)
    alt6                =models.CharField(max_length=70, blank=True)
  # CSS
    navbarTextColor    = models.CharField(max_length=20, blank=True,)
    navbarHoverTextColor    = models.CharField(max_length=20, blank=True,)
    navbarBackgroundColor = models.CharField(max_length=20, blank=True,)
    

class Footer(models.Model):
    title   =models.CharField(max_length=150, unique=True)
    row1    = models.CharField(max_length=200, blank=True)
    row2    = models.CharField(max_length=200, blank=True)
    row3    = models.CharField(max_length=200, blank=True)
    row4    = models.CharField(max_length=200, blank=True)
    row5    = models.CharField(max_length=200, blank=True)
    row6    = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

# Footer Css
class FooterCss(models.Model):
    title   =models.CharField(max_length=150, unique=True)
    footerTextColor    = models.CharField(max_length=20, blank=True,)
    footerHoverTextColor    = models.CharField(max_length=20, blank=True,)
    footerBackgroundColor = models.CharField(max_length=20, blank=True,)
    footerBackgroundImage = models.ImageField(upload_to='images/', default='images/footerbg.jpg')

    def __str__(self):
        return self.title

class SocialMediaIcon(models.Model):
    name    =models.CharField(max_length=100)
    icon    =models.ImageField(upload_to='images/')
    link    =models.URLField(max_length=300)

    def __str__(self):
        return self.name