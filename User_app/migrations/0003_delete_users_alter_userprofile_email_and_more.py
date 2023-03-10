# Generated by Django 4.0.2 on 2022-03-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0002_alter_userprofile_email_alter_userprofile_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
