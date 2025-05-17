from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def dynamic_url(request, id, name):
    print(f"This is the value that we got in the func → (id)")
    return render(request, "dynamic_url.html", context={"id": id, "name": name})


# class view
class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


def my_view(request):
    # Define context data
    context = {
        "title": "Welcome to My Website",
        "user": request.user,
        "items": ["Item 1", "Item 2", "Item 3"],
        "date": "2024-03-18",
        "number": 123.456,
    }
    # Pass context to the template
    return render(request, "basic.html", context)

def project(request):
    lucky_number = random.randint(0,99)
    context={"lucky_number": lucky_number}
    return render(request, "project/project.html", context)