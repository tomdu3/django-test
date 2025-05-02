from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def dynamic_url(request,id):
	print(f"This is the value that we got in the func -› {id}")
	return render (request,"dynamic_template.html", context={"id":id, "name":"Deepika"})