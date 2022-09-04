from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(unique=True, on_delete=models.CASCADE)

class Profile(Users):
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    bio=models.TextField()
    

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

class Comment(Users):
    time_stamp=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    content=models.TextField()

class Like(Users):

class PostView(Users):
     time_stamp=models.DateTimeField(auto_now_add=True)