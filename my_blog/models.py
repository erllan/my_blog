from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    blog = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    like = models.ManyToManyField(User, related_name='like_set', blank=True)
    genre = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='commentSet', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    toBlog = models.ForeignKey(Blog, on_delete=models.CASCADE)
