from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from core.admin import sky_admin_site

# Main URL Configuration for Sky Engineering Team Registry
urlpatterns = [
    # 🛠️ System Administration Portal
    path('admin/', sky_admin_site.urls),
    
    # 🔐 Authentication Hub (Login, Signup, JWT Simulation)
    path('accounts/', include('accounts.urls')),
    
    # 🏠 Central Dashboard & Core Services
    path('dashboard/', include('core.urls')),
    
    # 👥 Feature Apps (Student 1-5 Individual Tasks)
    path('teams/', include('teams.urls')),          # Student 1: Teams
    path('organisation/', include('organisation.urls')), # Student 2: Organisation
    path('messages/', include('messages_app.urls')),   # Student 3: Messages
    path('schedule/', include('schedule.urls')),       # Student 4: Schedule
    path('reports/', include('reports.urls')),         # Student 5: Reports
    
    # 📍 Root Redirect: Default entry point to the dashboard
    path('', RedirectView.as_view(url='/dashboard/', permanent=True)),
]
