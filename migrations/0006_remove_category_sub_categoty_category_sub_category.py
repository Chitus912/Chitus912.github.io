# Generated by Django 5.0.2 on 2024-03-13 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_categoty',
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='app.category'),
        ),
    ]
