from django.urls import path
from . import views

app_name = 'currency_convert'

urlpatterns = [
    path('convert/', views.currency_convert, name='currency_convert'),
]