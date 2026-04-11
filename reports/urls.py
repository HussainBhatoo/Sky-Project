from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.placeholder, name='reports_home'),
]
