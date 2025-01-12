from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy

from .models import NewUser
from .forms import NewUserForm



# class RegisterUserView(View):
#     def get(self, request):
#         user_form = NewUserForm()

#         context = {
#             'user_form': user_form
#         }

#         return render(request, 'accounts/register.html', context)
    
#     def post(self, request):
#         user_form = NewUserForm(request.POST)
        
#         if user_form.is_valid():
#             user_form.save()

#             messages.success(request, 'Qeydiyyatdan keçdiz')
#             return redirect('register_user')
        
#         else:
#             messages.error(request, user_form.errors)
#             return redirect('register_user')



class RegisterUserView(generic.CreateView):
    form_class = NewUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


# class SignView(View):

