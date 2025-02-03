import profile
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout

from .models import Profile, User
from .forms import (
    RegisterForm,
    LoginForm,
    ProfileForm,
)



class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()

        context = {
            'form': form
        }

        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Qeydiyyatdan keçdiz')
            return redirect('login')
        
        else:
            messages.error(request, form.errors)
            return redirect('register')


class UserSignView(View):
    def get(self, request):
        form = LoginForm()

        context = {
            'form': form
        }

        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None and user.is_active:
                    login(request, user)
                    messages.success(request, 'Uğurla daxil oldunuz')
                    return redirect('all_books')
            
            else:
                messages.error(request, 'Email və ya şifrə yanlışdır')
                return redirect('login')

        else:
            messages.error(request, 'Email və ya şifrə yanlışdırrrr')
            return redirect('login')



class UserSignOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Hesabdan çıxış edildi')
        
        return redirect('all_books')
    


class UserDeleteView(LoginRequiredMixin, View):
    def get_object(self, request):
        user = request.user
        
        return user
    
    def get(self, request):
        user = self.get_object(request=request)
        if user.is_employee == 0:
            user.is_active = False

            user.save()

            messages.success(request, 'Hesabınız silindi')
            return redirect('all_books')
        
        else:

            messages.info(request, 'Admin hesabı silinə bilməz')
            return redirect('all_books')

    def post(self, request):
        user = self.get_object(request=request)
        if user.is_employee == 0:
            user.is_active = False

            user.save()

            messages.success(request, 'Hesabınız silindi')
            return redirect('all_books')
        
        else:

            messages.info(request, 'Admin hesabı silinə bilməz')
            return redirect('all_books')



class ProfileView(LoginRequiredMixin, View):
    def get_object(self, request):
        profile = get_object_or_404(Profile, user=request.user)

        return profile

    def generate_profile_title(self, profile):
        email = profile.email
        profile_title = email.split('@')[0]

        return profile_title
    
    def get(self, request):
        profile = self.get_object(request=request)
        form = ProfileForm(instance=profile)
        profile_title = self.generate_profile_title(profile=profile)
        user = profile.user

        context = {
            'form': form,
            'profile': profile,
            "profile_title": profile_title,
            'user': user,
        }

        return render(request, 'accounts/profile.html', context)
    
    def post(self, request):
        profile = self.get_object(request=request)

        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile məlumatları yeniləndi')
            return redirect('profile')
        
        context = {
            'form': form
        }

        messages.error(request, "Formda səhvlər var. Məlumatları yenidən yoxlayın.")
        return render(request, 'accounts/profile.html', context)