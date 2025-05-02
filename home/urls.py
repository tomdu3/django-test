from django.urls import path
from .views import (
    index,
    about,
    contact,
    dynamic_url
    )

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path('<int:id>/', dynamic_url, name='dynamic_url')
]
