from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Post, Leave, Holiday, Employee,hrProfile
from django.views.generic import TemplateView,CreateView,DetailView
from .forms import *
from django.core.paginator import Paginator
from .filters import *
from .templatetags import doctor_extras
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


def EmployeeProfile(request,pk):
    employeeprofile=get_object_or_404(Employee,id=pk)
  
    context={
        'employee':employeeprofile,
    }
    return render(request,'profile/employeeprofile.html',context)


@login_required
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
    employees=Employee.objects.all()
    myFilter1=search_doctor(request.GET,queryset=employees)

    employees=myFilter1.qs
    paginated_list=Paginator(employees,2)
    page_number=request.GET.get('page')
    employee_page_obj=paginated_list.get_page(page_number)
    context={'employees':employees,'myFilter1':myFilter1,'employee_page_obj':employee_page_obj}
    return render(request,'payroll/employee_list.html',context)
    

def EmployeeProfile(request,pk):
    employee = Employee.objects.get(id=pk)
    return render(request,'profile/employeeProfile.html',{'employee':employee})

   
class ShowProfilePageView(DetailView):
	model = Employee
	template_name = 'profile/employeeProfile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(Employee, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context