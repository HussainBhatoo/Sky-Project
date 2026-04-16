from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('drafts/', views.draft_messages, name='draft_messages'),
    path('compose/', views.compose, name='compose'),
    path('compose/<int:message_id>/', views.compose, name='edit_draft'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('<int:message_id>/', views.message_detail, name='detail'),
]
