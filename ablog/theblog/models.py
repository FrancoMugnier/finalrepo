from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('detalle-articulo', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True, upload_to='images/')
    website_url=models.CharField(max_length=255, null=True, blank=True)
    facebook_url=models.CharField(max_length=255, null=True, blank=True)
    instagram_url=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        #return reverse('detalle-articulo', args=(str(self.id)))
        return reverse('home')

class post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to='images/')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True, null=True)
    #body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255)
    snippet=models.CharField(max_length=255)
    likes=models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('detalle-articulo', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(post, related_name='comments' , on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


