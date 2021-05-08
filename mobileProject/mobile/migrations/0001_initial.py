# Generated by Django 3.2 on 2021-05-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('specs', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
