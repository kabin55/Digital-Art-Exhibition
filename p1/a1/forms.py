from django import forms 
from a1.models import contact
from  django.contrib.auth.forms import  UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'email', 'message']
        
class SignupForms(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =  ['username', 'email', 'password1','password2']


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']