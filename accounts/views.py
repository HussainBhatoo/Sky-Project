from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Custom LoginView to redirect to dashboard upon success
class SkyLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        """Redirect to the dashboard after a successful login."""
        return reverse_lazy('dashboard')

# Custom User Registration View
class SkySignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Handle valid form submission."""
        response = super().form_valid(form)
        return response

def logout_view(request):
    """Custom logout view to handle session termination."""
    logout(request)
    return redirect('login')
