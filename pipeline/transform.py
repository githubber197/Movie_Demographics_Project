def transform_movie_data(movie_details):
    if not movie_details:
        return None
    
    transformed_data = {
        "title": movie_details.get("Title"),
        "year": int(movie_details.get("Year")[0:4]) if movie_details.get("Year") and len(movie_details.get("Year")) >= 4 else None,
        "genre": movie_details.get("Genre").split(", "),
        "imdb_rating": float(movie_details.get("imdbRating", "N/A")) if movie_details.get("imdbRating", "N/A") != "N/A" else None,
        "imdb_id": movie_details.get("imdbID"),
        "description": movie_details.get("Plot")
    }
    
    return transformed_data
if __name__ == "__main__":
    # paste a sample raw movie dict to test
    sample = {
        "Title": "Inception",
        "Year": "2010",
        "Genre": "Action, Adventure, Sci-Fi",
        "imdbRating": "8.8",
        "imdbID": "tt1375666",
        "Plot": "A thief who steals corporate secrets..."
    }
    print(transform_movie_data(sample))