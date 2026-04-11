from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [path('', views.placeholder, name='teams_list')]

