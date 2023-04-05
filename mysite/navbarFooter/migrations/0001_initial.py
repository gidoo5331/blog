# Generated by Django 3.2 on 2022-03-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('row1', models.CharField(blank=True, max_length=200)),
                ('row2', models.CharField(blank=True, max_length=200)),
                ('row3', models.CharField(blank=True, max_length=200)),
                ('row4', models.CharField(blank=True, max_length=200)),
                ('row5', models.CharField(blank=True, max_length=200)),
                ('row6', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FooterCss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('footerTextColor', models.CharField(blank=True, max_length=20)),
                ('footerHoverTextColor', models.CharField(blank=True, max_length=20)),
                ('footerBackgroundColor', models.CharField(blank=True, max_length=20)),
                ('footerBackgroundImage', models.ImageField(default='images/footerbg.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbrandName', models.CharField(max_length=40)),
                ('navbrandImage', models.ImageField(upload_to='images/')),
                ('link1', models.CharField(blank=True, max_length=70)),
                ('link2', models.CharField(blank=True, max_length=70)),
                ('link3', models.CharField(blank=True, max_length=70)),
                ('link4', models.CharField(blank=True, max_length=70)),
                ('link5', models.CharField(blank=True, max_length=70)),
                ('navbarTextColor', models.CharField(blank=True, max_length=20)),
                ('navbarHoverTextColor', models.CharField(blank=True, max_length=20)),
                ('navbarBackgroundColor', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='images/')),
                ('link', models.URLField(max_length=300)),
            ],
        ),
    ]
