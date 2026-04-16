from django.urls import path
from . import views

app_name = 'organisation'

urlpatterns = [
    path('', views.org_chart, name='org_chart'),
    path('dependencies/', views.dependencies, name='dependencies'),
    path('department/<int:dept_id>/', views.department_detail, name='department_detail'),
    path('department/<int:dept_id>/endorse/', views.toggle_department_endorsement, name='toggle_endorsement'),
]
