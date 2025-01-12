from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import NewUser


class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = NewUser 
        fields = ('username', 'email', 'password1', 'password2',)

        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email Address'})
    
    }