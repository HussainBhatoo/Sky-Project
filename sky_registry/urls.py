from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('core.urls')),
    path('teams/', include('teams.urls')),
    path('organisation/', include('organisation.urls')),
    path('messages/', include('messages_app.urls')),
    path('schedule/', include('schedule.urls')),
    path('reports/', include('reports.urls')),
    path('', RedirectView.as_view(url='/dashboard/', permanent=True)), # Redirect root to dashboard
]
