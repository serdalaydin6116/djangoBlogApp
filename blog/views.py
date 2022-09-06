from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def home(request):    

    posts=Post.objects.all()
    context= {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
    



    

