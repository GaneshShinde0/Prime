# Generated by Django 3.2.6 on 2021-08-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apibase',
            name='timeStamp',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='apibase',
            name='time_elapsed',
            field=models.CharField(max_length=35),
        ),
    ]
