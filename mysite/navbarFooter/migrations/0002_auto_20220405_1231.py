# Generated by Django 3.2 on 2022-04-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbarFooter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='alt5',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='navbar',
            name='alt6',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='navbar',
            name='link6',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
