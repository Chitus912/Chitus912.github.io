# Generated by Django 5.0.2 on 2024-03-27 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_classify_category_classify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='classify',
        ),
        migrations.DeleteModel(
            name='Classify',
        ),
    ]
