# Generated by Django 4.0.6 on 2023-08-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
