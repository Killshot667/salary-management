# Generated by Django 3.1 on 2020-11-23 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_auto_20201123_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]