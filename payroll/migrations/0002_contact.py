# Generated by Django 3.1.3 on 2020-11-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=300)),
            ],
        ),
    ]