from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=3000 , unique=True)
    slug = models.SlugField(max_length=3000 , unique=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, related_name='blog_post')
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    intro = models.TextField()
    content = models.TextField()
    banner = models.ImageField(upload_to='static/featured_image_%Y_%m_%d')
    image = models.ImageField(upload_to='static/featured_image_%Y_%m_%d')
    status = models.IntegerField(choices=STATUS, default=0)

    
    class Meta:
        ordering = ["-create_on"]

    def __str__(self):
        return self.title