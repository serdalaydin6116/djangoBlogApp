from django.db import models

from users.models import Users


class Post(Users):
    title= models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to='profile-pics', height_field=None, width_field=None, blank=true)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=70)
    slug=models.IntegerField()

    def __str__(self):
        return self.title
class Category(Post):
    name=models.CharField(max_length=70)   


class Comment(Post):
    # time_stamp=models.DateTimeField(auto_now_add=True)
    # last_updated=models.DateTimeField(auto_now=True)
    # content=models.TextField()

class Like(Post):

class PostView(Post):
    #  time_stamp=models.DateTimeField(auto_now_add=True)

