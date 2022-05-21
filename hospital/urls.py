from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('doctor_login', views.doctor_login),
    path('doctor_register', views.doctor_register),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]