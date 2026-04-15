from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('drafts/', views.draft_messages, name='draft_messages'),
    path('compose/', views.compose, name='compose'),
    path('<int:message_id>/', views.message_detail, name='detail'),
]
