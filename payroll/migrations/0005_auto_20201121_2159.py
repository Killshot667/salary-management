# Generated by Django 3.1 on 2020-11-21 16:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_merge_20201121_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hrprofile',
            name='department',
        ),
        migrations.AddField(
            model_name='employee',
            name='allowances_per_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='base_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='epf_deduction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='esi_deduction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='parent_hr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.hrprofile'),
        ),
        migrations.AddField(
            model_name='hrprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hrprofile',
            name='year_of_registration',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]