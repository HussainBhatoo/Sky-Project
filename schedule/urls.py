from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_calendar, name='calendar'),
    path('create/', views.schedule_create, name='create'),
    path('delete/<int:meeting_id>/', views.schedule_delete, name='delete'),
]
