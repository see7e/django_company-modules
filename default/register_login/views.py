from allauth.socialaccount.models import SocialAccount

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import CustomUser
from .forms import LoginForm, RegisterForm
from .utils import update_sidenav


# @update_sidenav
def index(request):
    # For now, the index has the same content as the dashboard
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = CustomUser.objects.create_user(username=email, email=email, password=password)

            # Log the user in
            login(request, user)

            # Render the index page
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register_login.html', {'form': form, 'register': True})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # Log the user in
                login(request, user)
                
                # Render the index page
                return redirect('/')
            else:
                # Invalid credentials, show an error message
                error_message = "Invalid email or password."
                return render(request, 'register_login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    
    return render(request, 'register_login.html', {'form': form})


def sso_login(request):
    if request.method == 'POST':
        # Get the SSO provider's user ID
        sso_user_id = request.POST['sso_user_id']
        
        # Find the user associated with the SSO provider's user ID
        try:
            social_account = SocialAccount.objects.get(uid=sso_user_id)
            user = social_account.user
            
            # Log the user in
            login(request, user)
            
            # Render the index page
            return redirect('/')
        except SocialAccount.DoesNotExist:
            # User not found, show an error message
            error_message = "User not found."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')