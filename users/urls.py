from django.urls import path
from .views import home


urlpatterns=[


    path('users/', home, name='home'),
   


]