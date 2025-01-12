from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import (
    RegisterForm,
    LoginForm,
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
    
    # def post(self, request):
    #     form = LoginForm(request.POST)

    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, email=email, password=password)

    #         print(f"Authenticated user: {user}")  # Burada yoxlayın

    #         if user is not None and user.is_active:
    #             login(request, user)
    #             messages.success(request, 'Uğurla daxil oldunuz')
    #             return redirect('all_books')
    #         else:
    #             messages.error(request, 'Email və ya şifrə yanlışdır')
    #             return redirect('login')
    #     else:
    #         messages.error(request, 'Email və ya şifrə yanlışdırrrr')
    #         return redirect('login')

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            print(user)
            print(email)
            print(password)


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






# # class UserRegisterView(generic.CreateView):
# #     form_class = UserForm
# #     template_name = 'accounts/register.html'
# #     success_url = reverse_lazy('login')


# class UserSignView(generic.ListView):
#     model = User
#     form_class = UserForm
#     fields = ['email', 'password']
#     template_name = 'accounts/login.html'