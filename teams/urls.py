from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('<int:team_id>/', views.team_detail, name='team_detail'),
    path('<int:team_id>/vote/', views.vote_team, name='vote_team'),
    path('<int:team_id>/disband/', views.disband_team, name='disband_team'),
]
