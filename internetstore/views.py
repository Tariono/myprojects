from django import forms
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm



def redirect_shop(request):
    return redirect('product_list_url', permanent=True)

class RegisterForm(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'


    def form_valid(self, form):
        form.save()
        login(self.request,authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))
        return super(RegisterForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterForm, self).form_invalid(form)
