
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('email/', views.send_email, name='email'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('assign/<int:id>/', views.assign, name='assign'),
    path('invoice/', views.invoice, name='invoice'),
]
