from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .models import Leave, Holiday, Employee,hrProfile,Contact
from django.views.generic import TemplateView,CreateView,DetailView
from .forms import *


from django.contrib.auth.decorators import login_required







class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class HrSignUpView(CreateView):
    model = User
    form_class = HrSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hr'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def HrProfile(request,pk):
    hrprofile=get_object_or_404(hrProfile,id=pk)
  
    context={
        'hr':hrprofile,
    }
    return render(request,'profile/hrProfile.html',context)


# def profile(request):
#   if request.method == 'POST':
#       u_form = UserUpdateForm(request.POST, instance=request.user)
#       d_form = EmployeeUpdateForm(request.POST,request.FILES,instance=request.user.doctor)
#       if u_form.is_valid() and d_form.is_valid():
#           u_form.save()
#           d_form.save()
#           messages.success(request, f'Your account has been updated!')
#           return redirect("home")

#   else:
#       u_form = UserUpdateForm(instance=request.user)
#       d_form = UpdateProfileForm(instance=request.user.doctor)

#   context = {
#       'u_form': u_form,
#       'd_form': d_form
#   }

#   return render(request, 'profile/editemployee.html', context)



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('payroll/login')
    else:
        return render(request,'payroll/login.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def view_list(request):
    employees = Employee.objects.all()
    return render(request,'payroll/employee_list.html',{'employees':employees})

def EmployeeProfile(request,pk):
    employee = Employee.objects.get(id=pk)
    return render(request,'payroll/employee_each.html',{'employee':employee})


def HrSignup(request):
    if request.method == 'GET':
        form = HrCreationForm()
        return render(request,'registration/signup_form.html',{'form':form})
    else:
        form = HrCreationForm(request.POST)
        
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            company_name = form.cleaned_data["company_name"]
            year_of_registration = form.cleaned_data["year_of_registration"]
            address = form.cleaned_data["address"]
            phone_number = form.cleaned_data["phone_number"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            full_name = str(first_name)+" "+str(last_name)

            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request,"username already taken")
                    return redirect('hr_signup')
                elif User.objects.filter(email = email).exists():
                    messages.info(request,"email already taken")
                    return redirect('hr_signup')
                else:
                    user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,is_hr=True)   
                    user.save()
                    hr = hrProfile(user = user,full_name=full_name,phone_number=phone_number,address=address,company_name=company_name,year_of_registration=year_of_registration)
                    hr.save()
                    messages.success(request,'company registered sucessfully')
                    print("company created")

                return redirect('login')
            else:
                messages.info(request,"email already taken")
                return redirect('hr_signup')
        
        else :
            messages.info(request,"please make sure you have filled all the fields correctly")
            return redirect('hr_signup')

def EmployeeSignup(request):
    pass

                
                

            
        

        
       
       