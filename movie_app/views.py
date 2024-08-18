from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from .forms import SignUpForm, AddMovieForm, LoginForm, DeleteMovieForm, movieform, ReviewForm
from .forms import AddMovieForm
from django.contrib import messages
import pandas as pd
from math import sqrt

import pandas as pd
from math import sqrt


import matplotlib.pyplot as plt
from math import ceil


# Create your views here.

def filterMovieByGenre():
    # filtering by genres
    allMovies = []
    genresMovie = Movie.objects.values('genres', 'id')
    genres = {item["genres"] for item in genresMovie}
    for genre in genres:
        movie = Movie.objects.filter(genres=genre)
        print(movie)
        n = len(movie)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allMovies.append([movie, range(1, nSlides), nSlides])
    params = {'allMovies': allMovies}
    return params


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                # group = Group.objects.get(name='Editor')
                group, created = Group.objects.get_or_create(name='Editor')
                user.groups.add(group)
                return HttpResponseRedirect('/login/')
        else:
            # not request.user.is_authenticated:
            fm = SignUpForm()
        return render(request, 'signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/home/')

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/')
        else:
            fm = LoginForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# def home(request):
#     params = filterMovieByGenre()
#     # params['recommended'] = generateRecommendation(request)
#     return render(request, 'home.html', params)

from django.shortcuts import render
from .models import Movie, Review  # Assuming you have a Movie model defined in models.py


def home(request):
    allMovies = Movie.objects.all()
    return render(request, 'home.html', {'allMovies': allMovies})
from django.shortcuts import render, redirect
from .forms import AddMovieForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddMovieForm, GenreForm


def addmovie(request):
    if request.method == 'POST':
        fm = AddMovieForm(request.POST, request.FILES)
        if fm.is_valid():
            movie = fm.save(commit=False)
            movie.added_by = request.user  # Set the added_by field with the current user
            movie.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('/')
    else:
        fm = AddMovieForm()

    # Create an instance of the GenreForm
    genre_form = GenreForm()

    return render(request, 'addmovie.html', {'form': fm, 'genre_form': genre_form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie

# Other view functions...

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie

def delete(request, id):
    mo = get_object_or_404(Movie, pk=id)  # Get the movie object or return 404 if not found
    if request.method == 'POST':
        mo.delete()
        messages.success(request, 'Movie Deleted Successfully')
        return redirect('home')  # Redirect to home or another appropriate URL
    return render(request, 'delete.html', {'movie': mo})

# def dashboard(request):
# if request.user.is_authenticated:
#     params = filterMovieByGenre()
#     params['user'] = request.user
#     if request.method == 'POST':
#         userid = request.POST.get('userid')
#         movieid = request.POST.get('movieid')
#         movie = Movie.objects.all()
#         u = User.objects.get(pk=userid)
#         m = Movie.objects.get(pk=movieid)
#         rfm = AddRatingForm(request.POST)
#         params['rform'] = rfm
#         if rfm.is_valid():
#             rat = rfm.cleaned_data['rating']
#             count = Rating.objects.filter(user=u, movie=m).count()
#             if (count > 0):
#                 messages.warning(request, 'You have already submitted your review!!')
#                 return render(request, 'dashboard.html', params)
#             action = Rating(user=u, movie=m, rating=rat)
#             action.save()
#             messages.success(request, 'You have submitted' + ' ' + rat + ' ' + "star")
#         return render(request, 'dashboard.html', params)
#     else:
#         # print(request.user.id)
#         rfm = AddRatingForm()
#         params['rform'] = rfm
#         movie = Movie.objects.all()
#         return render(request, 'dashboard.html', params)
# else:
#     return HttpResponseRedirect('/login/')
from django.shortcuts import render
from .models import Movie  # Assuming you have a Movie model defined in models.py

from django.shortcuts import render, redirect


def dashboard(request):
    allMovies = {}  # Initialize an empty dictionary to hold movies categorized by genres

    for movie in Movie.objects.all():
        if movie.genres in allMovies:
            allMovies[movie.genres].append(movie)
        else:
            allMovies[movie.genres] = [movie]

    return render(request, 'dashboard.html', {'allMovies': allMovies})


# def submit_rating(request):
#     if request.method == 'POST':
#         movie_id = request.POST.get('movieid')
#         user_id = request.POST.get('userid')
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             rating_value = form.cleaned_data['rating']
#             movie = Movie.objects.get(id=movie_id)
#             user = User.objects.get(id=user_id)
#             Rating.objects.create(movie=movie, user=user, rating=rating_value)
#             return redirect('submit_rating/')
#     return redirect('submit_rating/')

from django.shortcuts import render, redirect


from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


# @login_required
# def rate_movie(request):
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             movie_id = request.POST.get('movie_id')
#             movie = Movie.objects.get(pk=movie_id)
#             rating = form.save(commit=False)
#             rating.movie = movie
#             rating.user = request.user
#             rating.save()
#             messages.success(request, 'You successfully rated the Movie!')
#             return redirect('rate_movie_success')
#     else:
#         # Filter movies to only show those added by the current user
#
#         form = RatingForm()
#     return render(request, 'rate_movie.html', {'form': form})
#
# def rate_movie_success(request):
#     return render(request, 'rate_movie_success.html')


def edit(request, id):
    movi = Movie.objects.get(pk=id)
    form = movieform(request.POST or None, request.FILES, instance=movi)
    if form.is_valid():
        form.save()
        messages.success(request, 'Movie Updated successfully!')
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movi})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')


def profile(request):
    if request.user.is_authenticated:
        # "select sum(rating) from Rating where user=request.user.id"
        # r = Rating.objects.filter(user=request.user.id)
        # totalReview = 0
        # for item in r:
        #     totalReview += int(item.rating)
        # select count(*) from Rating where user=request.user.id"
        # totalwatchedmovie = Rating.objects.filter(user=request.user.id).count()

        return render(request, 'profile.html')
    else:
        return HttpResponseRedirect('/login/')


from django.shortcuts import render

from django.db.models import Q


# Create your views here.


def search_by_title(request):
    query = None
    movies = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(title=query) | Q(genres=query))
    return render(request, 'search.html', {'query': query, 'movies': movies})


from django.shortcuts import redirect


@login_required
def edit_movie(request, movie_id):
    # Ensure the movie belongs to the current user before allowing editing
    movie = Movie.objects.filter(id=movie_id, user=request.user).first()
    if movie:
        # Handle editing the movie
        return redirect('edit_movie_success')  # Redirect to a success page
    else:
        # Movie does not exist or does not belong to the user
        return redirect('edit_movie_failure')  # Redirect to a failure page or handle accordingly


from django.shortcuts import render
from .models import Movie

from django.shortcuts import render
from .models import Movie


def user_movie_list(request, user_id):
    user_movies = Movie.objects.filter(added_by=request.user)
    context = {
        'user_movies': user_movies
    }
    return render(request, 'user_movie_list.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages

#
# def rate_movie(request):
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             # Process the rating (save to database, etc.)
#             messages.success(request, 'You successfully rated the Movie!')
#             return redirect('dashboard')
#     else:
#         form = RatingForm()
#     return render(request, 'rate_movie.html', {'form': form})
#
# def rate_movie_success(request):
#
#     return render(request, 'rate_movie_success.html')
from django.shortcuts import render, redirect
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import RatingForm
# from .models import Reviews
#
# import requests
#
#
def rate_movie(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            movie = form.cleaned_data['movie']

            # Check if the user is authenticated
            if request.user.is_authenticated:
                # If authenticated, associate the rating with the user
                user = request.user
            else:
                # If not authenticated, set user to None (anonymous)
                user = None

            # Delete previous rating by the user for the same movie if it exists
            Review.objects.filter(user=user, movie=movie).delete()

            rating = form.save(commit=False)
            rating.user = user
            rating.save()
            messages.success(request, 'You successfully rated the Movie!')
            return redirect('rate_movie_success')
    else:
        form = ReviewForm()
    return render(request, 'rate_movie.html', {'form': form})


from django.shortcuts import render
from .models import Review


def rate_movie_success(request):
    # Retrieve the last rating submitted by the current user
    user_rating = Review.objects.filter(user=request.user).last()

    return render(request, 'rate_movie_success.html', {'user_rating': user_rating})


from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Movie, Review

#
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ReviewForm
# from .models import Movie, Review
#
# def add_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Review added successfully!')
#             return redirect('review_success')  # Redirect to a success page
#     else:
#         form = ReviewForm()
#
#     movies_with_reviews = []
#     for movie in Movie.objects.all():
#         reviews = Review.objects.filter(movie=movie)
#         movies_with_reviews.append({'movie': movie, 'reviews': reviews})
#
#     return render(request, 'review.html', {'form': form, 'movies_with_reviews': movies_with_reviews})
#
#
# from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReviewForm

from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Movie

from django.contrib import messages

from django.contrib import messages

from django.contrib import messages
from django.urls import reverse

def add_review(request, movie_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                # Set the movie_id for the new review
                form.instance.movie_id = movie_id
                form.save()
                messages.success(request, 'Review added successfully.')  # Add success message
                return redirect(reverse('show_reviews', kwargs={'movie_id': movie_id}) + '?success=True')  # Redirect with success parameter
            except IntegrityError:
                # Handle IntegrityError if movie_id is not valid
                return HttpResponse("Invalid movie ID")
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie_id': movie_id})


from django.shortcuts import render
from .models import Review

from django.shortcuts import render
from .models import Review


def show_reviews(request, movie_id):
    success_message = None
    if 'success' in request.GET and request.GET['success'] == 'True':
        success_message = 'Review added successfully.'
    reviews = Review.objects.filter(movie_id=movie_id)
    return render(request, 'show_reviews.html', {'reviews': reviews, 'success_message': success_message})

def review_success(request):
    return render(request, 'review_success.html')
    # Retrieve all movies and their respective ratings and descriptions

from django.shortcuts import render, get_object_or_404
from .models import Movie

from django.shortcuts import render
from .models import Movie

# views.py
from django.shortcuts import render
from .models import Movie  # Assuming you have a Movie model defined

from django.shortcuts import render

from django.shortcuts import render
from .forms import GenreForm

from django.shortcuts import render
from .forms import GenreForm

from django.shortcuts import render
from .models import Movie

def genre_view(request, genre):
    movies = Movie.objects.filter(genres__icontains=genre)  # Assuming genres are stored as a comma-separated string
    return render(request, 'bb.html', {'movies': movies, 'genre': genre})

from django.shortcuts import render
from .models import Movie

# def genre_view(request, genre):
#     # Query movies by genre
#     movies = Movie.objects.filter(genres__name=genre)  # Assuming genre is stored as a name in the Genre model
#     return render(request, 'genre_view.html', {'movies': movies, 'genre': genre})




from django.shortcuts import render
from .models import Movie, Genre

def navbar(request):
    genres = Genre.objects.all()
    return render(request, 'navbar.html', {'genres': genres})


