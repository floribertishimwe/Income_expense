# Generated by Django 4.0.6 on 2023-08-23 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
    ]