
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.About, name='about'),
    path('dep/<int:id>/', views.detail, name='detail'),
    path('doc/<int:id>/', views.doc_detail, name='doc_detail')
]