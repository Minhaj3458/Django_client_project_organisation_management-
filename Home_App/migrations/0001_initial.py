# Generated by Django 4.0.2 on 2022-02-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('email', models.EmailField(max_length=100, verbose_name='Email address')),
                ('phone1', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number1')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number1')),
                ('user_name', models.CharField(max_length=50, null=True, verbose_name='User Name')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Date Time')),
            ],
        ),
    ]