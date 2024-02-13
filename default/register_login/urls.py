from django.urls import path
from . import views


app_name = 'register_login'

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('sso-login/', views.sso_login, name='sso_login'),
    path('register/', views.register, name='register'),
    path('home/', views.index, name='home'),
]
