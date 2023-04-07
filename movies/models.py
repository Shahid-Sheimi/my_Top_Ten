from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from .models import User



class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    poster_url = models.URLField()
    description = models.TextField()
    user_rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    user_rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    top_ten_movies = models.ManyToManyField(Movie, blank=True, related_name='top_ten_movies')
    top_ten_songs = models.ManyToManyField(Song, blank=True, related_name='top_ten_songs')




class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    



