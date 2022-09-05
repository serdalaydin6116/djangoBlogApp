from django.db import models




class Post(models.Model):
    title= models.CharField(max_length=70)
    slug=models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to='profile-pics', height_field=None, width_field=None, blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=70)

    def __str__(self):
        return self.title




