from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world!, You are in blog's index page")

def detail(request,id):
    return HttpResponse(f"You are viewing post detail page. And the the ID is {id}")
    
def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is the new urls")