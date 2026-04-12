from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('<int:message_id>/', views.message_detail, name='detail'),
]
