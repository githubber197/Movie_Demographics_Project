def transform_movie_data(movie_details):
    if not movie_details:
        return None
    
    transformed_data = {
        "title": movie_details.get("Title"),
        "year": int(movie_details.get("Year")[0:4]) if movie_details.get("Year") and len(movie_details.get("Year")) >= 4 else None,
        "genre": movie_details.get("Genre").split(", ") if movie_details.get("Genre") and movie_details.get("Genre") != "N/A" else [],
        "imdb_rating": float(movie_details.get("imdbRating", "N/A")) if movie_details.get("imdbRating", "N/A") != "N/A" else None,
        "imdb_id": movie_details.get("imdbID"),
        "description": movie_details.get("Plot") if movie_details.get("Plot") != "N/A" else None
    }
    
    return transformed_data
