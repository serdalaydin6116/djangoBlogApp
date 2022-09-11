from django.urls import path
from .views import home, user_login, user_register, user_logout, user_profile

# from django.contrib.auth import views as auth_views




urlpatterns=[


    
   
    path('', home, name='home'),
    # path('special/', special, name='special'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path("profile/", user_profile, name="profile"),
   


]