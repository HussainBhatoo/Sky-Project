from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
    path('export/csv/', views.export_csv, name='export_csv'),
]
