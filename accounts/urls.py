from django.urls import path
from .views import SkyLoginView, SkySignupView, logout_view

urlpatterns = [
    # Auth Routes
    path('login/', SkyLoginView.as_view(), name='login'),
    path('signup/', SkySignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]
