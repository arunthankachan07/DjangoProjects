# Generated by Django 3.2 on 2021-04-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desig', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
