from django.db import models
from django.utils import timezone

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    post = models.ForeignKey(BoardModel,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

class Reply(models.Model):
    name = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    target = models.ForeignKey(Comment,on_delete=models.CASCADE)
    is_publoc = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
