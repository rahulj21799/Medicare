# Generated by Django 3.0.2 on 2020-08-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicareOne', '0017_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrasturcture',
            name='description',
            field=models.CharField(blank=True, default='', max_length=50000, verbose_name='Description'),
        ),
    ]
