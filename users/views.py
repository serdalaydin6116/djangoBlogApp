from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/base.html')


@login_required
def login(request):
    return render(request, "registration/login.html")





def register(request):
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
