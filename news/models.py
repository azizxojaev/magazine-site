from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class New(models.Model):
    image = models.ImageField(upload_to='news/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(New, self).save(*args, **kwargs)

    def __str__(self):
        return self.title