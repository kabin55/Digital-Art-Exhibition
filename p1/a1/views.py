from django.shortcuts import render, redirect
from a1.forms import contactForm ,SignupForms,LogInForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message or redirect to a thank you page
            return redirect('thank_you_page')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'You have been logged in successfully!')
            # login(request, user)
            # messages.success(request, f'Account created for {user}!')
            return redirect('profile/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LogInForm()
    return render(request,'login.html', {'form': form})
    
def profile(request):
    return render(request,'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Account created for {username}!')
            # login(request, user)
           
            return redirect('login/')  # Redirect to the home page after successful 
        else:
            messages.error(request, 'Error creating account. Please correct the errors below.')
    else:
        form = SignupForms()
    return render(request, 'signup.html', {'form': form})
