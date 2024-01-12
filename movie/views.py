from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    searchTerm = request.GET.get('searchMovie') #whatever the input name attribute is in the template
    if searchTerm:
        movies = Movie.objects.filter(title__icontains= searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

    
def about(request):
    return HttpResponse('<h1>This is the about page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
