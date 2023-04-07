import requests

TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOWNiYTZkZTY5NzhkYTBjODIzYTQyYWMxMGQ4Zjg4OSIsInN1YiI6IjY0MmU3NWY5MmRjNDRlMDBiZWIwOTFkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9zYxgnjTAEAM55Gg7D3PwbMMkQudnyKcDrwohGwZyow'  # Replace with your actual TMDB API key


def search_movies(query):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}'
    response = requests.get(url)
    return response.json()




def get_movie_details(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract movie details from the API response
    movie_name = data['original_title']
    movie_id = data['id']
    movie_title = data['title']

    return movie_name, movie_id, movie_title

def get_movie(request, movie_id):
    # Call the function to get movie details
    movie_name, movie_id, movie_title = get_movie_details(movie_id)

    # Return the extracted movie details to the client
    return JsonResponse({'movie_name': movie_name, 'movie_id': movie_id, 'movie_title': movie_title})

