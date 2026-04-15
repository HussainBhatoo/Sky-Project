from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import SkyLoginView, SkySignupView, logout_view, SkyForgotPasswordView

app_name = 'accounts'

urlpatterns = [
    # Auth Routes
    path('login/', SkyLoginView.as_view(), name='login'),
    path('signup/', SkySignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),

    # Simplified Forgot Password (Anonymous)
    path('forgot-password/', SkyForgotPasswordView.as_view(), name='forgot_password'),

    # Authenticated User Password Change
    path('password-change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change_form.html',
             success_url=reverse_lazy('accounts:password_change_done')
         ), 
         name='password_change'),
    path('password-change/done/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'
         ), 
         name='password_change_done'),
]
