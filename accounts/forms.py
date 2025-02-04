from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import (
    User,
    Profile
)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ('email', 'password1', 'password2',)

        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email Address'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['email'].label = 'Emaili əlavə edin'
        self.fields['password1'].label = 'Şifrə təyin edin'
        self.fields['password2'].label = 'Şifrəni təyin edin'



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['email'].label = 'Emaili yazın'
        self.fields['password'].label = 'Şifrəni yazın'



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('account_balance', 'profile_image')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['account_balance'].label = 'Balans'
        self.fields['profile_image'].label = 'Profil Şəkli seçin'
