from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add, name='add'),
    path('share/', views.share, name='share'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('view/', views.view, name='view'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor2/', views.doctor2, name='doctor2'),
    
]
