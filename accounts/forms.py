from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ('email', 'password1', 'password2',)

        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email Address'})
    
    }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email:
    #         raise forms.ValidationError("Email sahəsi boş ola bilməz")
    #     return email
    