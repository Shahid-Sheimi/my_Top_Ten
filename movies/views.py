from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movie, Song, UserProfile
from .serializers import MovieSerializer, SongSerializer, UserProfileSerializer
from .tmdb_client import search_movies, get_movie_details
from django.shortcuts import render,redirect
from .models import Movie,Song,UserProfile,User
import tmdbv3api







def Index(request):
    return render(request,'index.html')

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

    def post(self, request, *args, **kwargs):
        data = request.data
        title = data.get('title')
        release_date = data.get('release_date')
        poster_url = data.get('poster_url')
        description = data.get('description')
        user_rating = data.get('user_rating')
        user_id = request.user

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']

        # Create a new User instance
        user = User(username=username, first_name=first_name, last_name=last_name, password=password)
        user.save()

        return redirect('signin')  # Redirect to sign-in page

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if user exists in the database
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('home')  # Redirect to home page upon successful sign-in
        except User.DoesNotExist:
            # Handle invalid credentials (e.g., show an error message)
            pass

    return render(request, 'signin.html')



def add_to_top_ten(request, movie_id):
    # Retrieve movie details from TMDB API using movie_id
    tmdb_api_key = 'YOUR_TMDB_API_KEY'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}'
    response = requests.get(url)
    movie_data = response.json()

    # Create a new Movie object and save it to the database
    movie = Movie(
        title=movie_data['title'],
        description=movie_data['overview'],
        poster_path=movie_data['poster_path']
        # ... add other fields as needed
    )
    movie.save()

    # Add the movie to the user's top ten movies list
    user = request.user  # Assuming user is logged in
    user.profile.top_ten_movies.add(movie)

    return redirect('top_ten_movies')  # Redirect to user's top ten movies list page    


def reorder_top_ten(request):
    if request.method == 'POST':
        top_ten_ids = request.POST.getlist('movie_id[]')  # Get the list of movie IDs from the form

        # Update the order of movies in the user's top ten movies list
        user = request.user  # Assuming user is logged in
        user_profile = user.profile  # Assuming user profile model has a top_ten_movies field
        user_profile.top_ten_movies.clear()  # Clear the current top ten movies list

        # Loop through the list of movie IDs and add them to the top ten movies list in the desired order
        for movie_id in top_ten_ids:
            movie = Movie.objects.get(id=movie_id)
            user_profile.top_ten_movies.add(movie)

        return redirect('top_ten_movies')  # Redirect to user's top ten movies list page

    return render(request, 'reorder_top_ten.html')  # Render the reorder page with the top ten movies list

def edit_top_ten(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST':
        # Get updated data from the form
        title = request.POST['title']
        release_date = request.POST['release_date']
        # Update the movie data
        movie.title = title
        movie.release_date = release_date
        movie.save()  # Save the updated movie data

        return redirect('top_ten_movies')  # Redirect to user's top ten movies list page

    context = {'movie': movie}
    return render(request, 'edit_top_ten.html', context)  # Render the edit page with the movie data



def movie_detail(request, movie_id):
    # Retrieve the movie details from TMDB API using TMDBV3API
    tmdb = tmdbv3api.TMDb()
    tmdb.api_key = 'YOUR_TMDB_API_KEY'  # Replace with your TMDB API key
    movie = tmdb.get_movie(movie_id)

    context = {'movie': movie}
    return render(request, 'movie_detail.html', context)