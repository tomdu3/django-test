from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email, name='send_email'),
    path('sent/', views.email_sent, name='email_sent'),
]