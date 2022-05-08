import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from account.forms import LoginForm, RegisterForm
from account.service import create_user


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = reverse_lazy('home')
                return redirect(redirect_url)
            else:
                messages.error(request, 'Bad Credentials', extra_tags='danger')
        return render(request, self.template_name, {'form': form})


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                create_user(form)
                return redirect('auth:login')
            except Exception as e:
                logging.error(e)
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})
