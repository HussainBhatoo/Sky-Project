from django.urls import path
from . import views

app_name = 'organisation'

urlpatterns = [path('departments/', views.placeholder, name='departments'), path('dependencies/', views.placeholder, name='dependencies')]

