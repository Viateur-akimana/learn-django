from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .form import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            
            # Log the user in
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    # Render the registration form in case of GET or invalid POST
    return render(request, 'accounts/register.html', {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Redirect to the 'next' parameter if present, else to 'home'
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid credentials"
            return render(request, "accounts/login.html", {'error': error_message})
    
    # Render login form in case of GET request
    return render(request, "accounts/login.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')

@login_required
def home_view(request):
    return render(request, "home/home.html")



class ProtectedView(LoginRequiredMixin,View):
    login_url='/login/'
    redirect_field_name='redirect_to'
    
    def get(self,request):
        return render(request,'registration/protected.html')
    