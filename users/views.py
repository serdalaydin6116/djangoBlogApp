from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from blog.models import Post 
from .forms import UserUpdateForm, ProfileUpdateForm, RegistrationForm

def home(request):    

    posts=Post.objects.all()
    context= {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# @login_required
# def special(request):
#     return render(request, "users/special.html")





def user_register(request):
   
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.method=='POST':
    #     form=UserCreationForm(request,POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)

        login(request, user)
        return redirect('home')
    else:
        form=UserCreationForm()

    context = {
            'form': form
    }
    return render(request, "registration/register.html", context)



def user_login(request):
    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request, user)
        messages.success(request,'You logged in successfully')
        return redirect('home')
    context = {
            'form': form
    }

    return render(request, 'registration/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def user_password_change(request):
    if request.method == 'POST':
       
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)


def user_profile(request):
    
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST or None, files=request.FILES, instance=request.user.profile )
    
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, "Your profile has been updated successfully!")
        return redirect('home')
    
    context = {
        "user_form" : user_form,
        "profile_form" : profile_form    
    }
    return render(request, "registration/profile.html", context)




