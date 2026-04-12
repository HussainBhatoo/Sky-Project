from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('audit/', views.audit_log, name='audit_log'),
    path('profile/', views.profile_view, name='profile'),
]
