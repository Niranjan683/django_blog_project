from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import Post
from django.core.paginator import Paginator
from .forms import ContactForm
# Create your views here.
# static demo data
#posts=[
#    {'id':1,'title':'Post 1', 'Content': " Content of Post 1"},
#    {'id':2,'title':'Post 2', 'Content': " Content of Post 2"},
#    {'id':3,'title':'Post 3', 'Content': " Content of Post 3"},
#    {'id':4,'title':'Post 4', 'Content': " Content of Post 4"},
#    ]


def index(request):
    blog_title = "Latest Posts" 
    # getting data from post model
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,5)
    page_number=request.GET.get('page_no')
    page_obj = paginator.get_page(page_number)

    return render(request,'index.html',{'blog_title': blog_title, 'page_obj':page_obj})


def detail(request,slug):
    #getting static data 
    #post=next((item for item in posts if item['id']==id),None)
 
    try:
    # getting data from model by post id
        post=Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Doesn't Exist")
 
    #logger=logging.getLogger("TESTING")
    #logger.debug(f"post variable is {post}")

    return render (request,'detail.html',{'post':post,'related_posts':related_posts})    


def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("This is the new urls")

def contact_view(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        
        if form.is_valid():
            logger = logging.getLogger("TESTING")
            logger.debug(f"POST data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
    return render (request,'contact.html')    