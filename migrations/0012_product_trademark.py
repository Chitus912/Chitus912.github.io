# Generated by Django 5.0.2 on 2024-03-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_shippingaddress_emails_shippingaddress_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='trademark',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
