from django.urls import path
from .views import home, special, user_login, user_register, user_password_change

# login, register


urlpatterns=[


    # path('', home, name='home'),
   
    path('', home, name='home'),
    path('special/', special, name='special'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
   


]