# Generated by Django 3.2 on 2021-05-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_auto_20210508_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='price_total',
            field=models.FloatField(null=True),
        ),
    ]
