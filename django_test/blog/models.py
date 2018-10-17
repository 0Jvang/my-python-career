from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200, default='无简介')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    change_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20, default='root')
    views = models.IntegerField(default=0)

    class Meta:
        db_table = 'Post'

class User(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=200)
    address = models.CharField(max_length=20)