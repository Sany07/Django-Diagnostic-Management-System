
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.About, name='about'),
    path('<int:id>/', views.detail, name='detail')
]