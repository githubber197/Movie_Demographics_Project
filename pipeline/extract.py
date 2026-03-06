
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("OMDB_API_KEY")


def fetch_movies(title):
    url = f"http://www.omdbapi.com/?s={title}&apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data.get("Search", [])  
        else:
            print(f"No results found for: {title}")
            return []                      
    else:
        print(f"HTTP Error: {response.status_code}")
        return []
def fetch_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data  
        else:
            print(f"No details found for IMDb ID: {imdb_id}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None
if __name__ == "__main__":
    movies = fetch_movies("Inception")
    print(movies)
    if movies:
        movie_details = fetch_movie_details(movies[0].get("imdbID"))
        print(movie_details)