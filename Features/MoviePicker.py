import requests
import random

def get_random_movie_or_tv_show():
    # Define the base URL and API key for the Movie Database API
    url = "https://api.themoviedb.org/3"
    api_key = "k_12345678"

    # Define the endpoints for getting popular movies and TV shows
    movie_endpoint = "/movie/popular"
    tv_show_endpoint = "/tv/popular"

    # Generate a random number to determine whether to get a movie or TV show
    random_number = random.randint(1, 2)

    # Use the Movie Database API to get a random popular movie or TV show
    if random_number == 1:
        # Get a random popular movie
        params = {"api_key": api_key, "language": "en-US", "page": "1"}
        response = requests.get(url + movie_endpoint, params=params).json()
        random_movie = random.choice(response["results"])
        return random_movie["title"]

    else:
        # Get a random popular TV show
        params = {"api_key": api_key, "language": "en-US", "page": "1"}
        response = requests.get(url + tv_show_endpoint, params=params).json()
        random_tv_show = random.choice(response["results"])
        return random_tv_show["name"]