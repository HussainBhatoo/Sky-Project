from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserSignupForm
from core.models import AuditLog

class SkyLoginView(LoginView):
    """
    SkyLoginView handles the authentication process for Sky employees.
    It utilizes the official Sky Spectrum design tokens and redirects users 
    to the centralized dashboard upon successful verification.
    """
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        """Redirect to the dashboard after a successful login."""
        # Log successful login action
        AuditLog.objects.create(
            actor_user=self.request.user,
            action_type='UPDATE',
            entity_type='User',
            entity_id=self.request.user.id,
            change_summary=f"User '{self.request.user.username}' logged in successfully."
        )
        return reverse_lazy('core:dashboard')

class SkySignupView(CreateView):
    """
    SkySignupView handles the creation of new official Sky Registry accounts.
    It implements the mandatory corporate email requirement from the 
    coursework implementation plan and ensures data integrity.
    """
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        """
        Processes a valid form submission by saving the new user object 
        and redirecting them to the login portal.
        """
        response = super().form_valid(form)
        return response

class SkyForgotPasswordView(TemplateView):
    """
    Simplified Forgot Password view that displays a static contact message.
    Used to satisfy coursework requirements without full SMTP complexity.
    """
    template_name = 'registration/forgot_password.html'

def logout_view(request):
    """
    Custom logout handler that terminates the current Django session 
    and clears authentication tokens before redirecting to the login screen.
    """
    if request.user.is_authenticated:
        # Log logout action before the session is cleared
        AuditLog.objects.create(
            actor_user=request.user,
            action_type='UPDATE',
            entity_type='User',
            entity_id=request.user.id,
            change_summary=f"User '{request.user.username}' logged out."
        )
    logout(request)
    return redirect('accounts:login')
