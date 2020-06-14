from django.db import models

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
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=BoardModel, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.text
