# Generated by Django 3.0 on 2021-05-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developerusers',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='developerusers',
            name='mail_address',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]