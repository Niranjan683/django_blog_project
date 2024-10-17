from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

def detail(request,id):
    return HttpResponse(f"You are viewing post detail page. And the the ID is {id}")
    
def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new urls")