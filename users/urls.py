from django.urls import path
from .views import home, special, register

# login, register


urlpatterns=[


    # path('', home, name='home'),
   
    path('', home, name='home'),
    path('special/', special, name='special'),
    # path('login/', login, name='login'),
    path('register/', register, name='register'),
   


]