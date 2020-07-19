from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    name = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    target = models.ForeignKey(BoardModel, null=True, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Reply(models.Model):
    name = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    target = models.ForeignKey(Comment,on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
