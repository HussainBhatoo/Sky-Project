from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserSignupForm

class SkyLoginView(LoginView):
    """
    SkyLoginView handles the authentication process for Sky employees.
    It utilizes the official Sky Spectrum design tokens and redirects users 
    to the centralized dashboard upon successful verification.
    """
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        """Redirect to the dashboard after a successful login."""
        return reverse_lazy('core:dashboard')

class SkySignupView(CreateView):
    """
    SkySignupView handles the creation of new official Sky Registry accounts.
    It implements the mandatory corporate email requirement from the 
    coursework implementation plan and ensures data integrity.
    """
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        Processes a valid form submission by saving the new user object 
        and redirecting them to the login portal.
        """
        response = super().form_valid(form)
        return response

def logout_view(request):
    """
    Custom logout handler that terminates the current Django session 
    and clears authentication tokens before redirecting to the login screen.
    """
    logout(request)
    return redirect('login')
