from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
     path('login/', views.login_views, name='login'),
      path('signup/', views.signup_views, name='signup'),
      
]