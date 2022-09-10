from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'users/base.html')


@login_required
def special(request):
    return render(request, "users/special.html")





def register(request):
   
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




# class Login

# Create your views here.
