from django.shortcuts import render
# reverse_lazy is in case someone is logged in or out where they should go
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
