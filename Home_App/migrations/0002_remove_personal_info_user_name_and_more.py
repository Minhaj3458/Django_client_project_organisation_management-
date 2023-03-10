# Generated by Django 4.0.2 on 2022-02-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_info',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='Email address'),
        ),
    ]
