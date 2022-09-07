from django.shortcuts import render, redirect
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


def blog_create(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={
        'form' :form
    }
    return render(request, 'blog/post_create.html', context)


def blog_update (request, id):
    post= Post.objects.get(id=id)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={ 
        
        'form': form,
    }
    return render(request,'blog/post_update.html', context )

def blog_delete(request, id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        post.delete()
        return redirect ('home')
    return render (render, 'blog/post_delete')

    



    

