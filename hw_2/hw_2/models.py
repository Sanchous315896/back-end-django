from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    producer = models.CharField(max_length=200)
    duration = models.IntegerField()


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)
    author = models.CharField(max_length=200)
