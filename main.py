from pipeline.extract import fetch_movies, fetch_movie_details
from pipeline.transform import transform_movie_data
from pipeline.load import load_movies

if __name__ == "__main__":
    # Step 1 - Extract
    raw_movies = fetch_movies("Inception")
    
    # Step 2 - Transform each movie
    transformed = []
    for movie in raw_movies:
        details = fetch_movie_details(movie.get("imdbID"))
        clean = transform_movie_data(details)
        if clean:
            transformed.append(clean)
    
    # Step 3 - Load
    load_movies(transformed)
    print("Pipeline complete!")