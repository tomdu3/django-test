from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi.. from Django Server")


from django.http import HttpResponse


def about(request):
    html_content = "<h1>Hii.. from Django Server | This is a <b>About Page... </b> <br> <p> This about page can be used to see the about section.</p>"
    return HttpResponse(html_content)
