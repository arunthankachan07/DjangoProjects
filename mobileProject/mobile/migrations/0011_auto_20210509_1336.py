# Generated by Django 3.2 on 2021-05-09 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0010_auto_20210509_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_time',
        ),
    ]