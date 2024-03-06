from django.http import HttpResponse
from django.shortcuts import render
from movie.models import Movie, Article


# Create your views here.
def movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'main.html', context)


def movie_by_id(request, id):
    movie_single = Movie.objects.get(pk=id)
    context = {"movie_single": movie_single}
    return render(request, 'main.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'main.html', context)


def articles_by_id(request, id):
    article_single = Article.objects.get(pk=id)
    context = {"article_single": article_single}
    return render(request, 'main.html', context)
