from django.urls import path
from .views import (
    index,
    about,
    contact,
    dynamic_url,
    HomeView,
    my_view,
    project,
)

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("<int:id>/<str:name>/", dynamic_url, name="dynamic_url"),
    path("home/", HomeView.as_view(), name="home2"),
    path("my_view/", my_view, name="my_view"),
    path("project/", project, name="project"),
]
