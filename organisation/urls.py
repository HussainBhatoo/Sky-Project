from django.urls import path
from . import views

app_name = 'organisation'

urlpatterns = [
    path('', views.placeholder, name='org_chart'),
    path('dependencies/', views.placeholder, name='dependencies'),
]
