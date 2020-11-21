from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.admin.widgets import AdminDateWidget

from .models import ( User,Employee,hrProfile)


class HrSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hr = True
        user.save()
        hr = hrProfile.objects.create(user=user)
        return user


class EmployeeSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        return user

class UserUpdateForm(forms.ModelForm):
	
  email = forms.EmailField()
  first_name=forms.CharField()
  last_name=forms.CharField()	
  class Meta:
      model = User
      fields = ['username', 'email','first_name','last_name']

class EmplyeeUpdateForm(forms.ModelForm):
	profile_pic = forms.ImageField(widget=forms.FileInput,)
	class Meta:
		model = Employee
		fields = ['profile_pic','phone_number','address']


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

YEARS= [x for x in range(1940,2021)]

class HrCreationForm(forms.Form):
    phone_number = forms.CharField(max_length=12)
    address=forms.CharField(max_length=255)
    company_name = forms.CharField(max_length=255)
    year_of_registration = forms.DateField()
    username = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'retype password'
        self.fields['email'].widget.attrs['placeholder'] = 'company mail-id'
        self.fields['year_of_registration'].widget.attrs['placeholder'] = 'year of registration (mm/dd/yyyy)'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'phone number'
        self.fields['address'].widget.attrs['placeholder'] = 'HQ address'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Company name'
        self.fields['first_name'].widget.attrs['placeholder'] = 'admin first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'admin last name'



