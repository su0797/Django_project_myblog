from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path('join/', views.Join.as_view(), name='join'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]