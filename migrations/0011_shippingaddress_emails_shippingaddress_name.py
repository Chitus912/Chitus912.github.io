# Generated by Django 5.0.2 on 2024-03-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='emails',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
