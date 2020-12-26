# Generated by Django 3.0.2 on 2020-02-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicareOne', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='course',
            field=models.CharField(default='', max_length=20, verbose_name='Selected Course'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='mobile',
            field=models.IntegerField(default=0, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Full Name'),
        ),
    ]
