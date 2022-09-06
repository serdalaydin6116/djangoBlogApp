from django.urls import path
from .views import home

urlpatterns=[
    path('', home, name='home'),
    # path('list/', list, name='list'),
    # path('update/<int:id>', todo_update, name='update'),
    # path('delete/<int:id>', todo_delete, name='delete')


]