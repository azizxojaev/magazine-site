from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Tag(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.user.username
    

class New(models.Model):
    image = models.ImageField(upload_to='news/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(New, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class NewsView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"
    

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username}'s comment"


class ReplyComment(models.Model):
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username}'s reply to {self.reply_to.user.user.username}"
    

class Contact(models.Model):
    contact_info = models.TextField()
    location = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)