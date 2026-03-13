from load_movielens import read_links
from pathlib import Path
import pandas as pd
from load import get_connection

BASE_DIR = Path(__file__).parent.parent
def load_ratings():
    values = pd.read_csv(BASE_DIR / "data/raw/ratings.csv", usecols=["userId", "movieId", "rating"])
    conn = get_connection()
    cursor = conn.cursor()
    links = read_links()
    movie_lookup = {}
    cursor.execute("SELECT movie_id, tmdb_id FROM movies")
    for movie_id, tmdb_id in cursor.fetchall():
        movie_lookup[tmdb_id] = movie_id
    values["imdb_id"] = values["movieId"].map(links)
    values["db_movie_id"] = values["imdb_id"].map(movie_lookup)
    values = values.dropna(subset=["db_movie_id"])
    converted_values = list(zip(values["userId"], values["db_movie_id"].astype(int), values["rating"]))
    cursor.executemany(
        "INSERT INTO reviews (user_id, movie_id, movie_rating) VALUES (%s, %s, %s)",
        converted_values
    )  
    
    print(f"Ratings loaded successfully from {BASE_DIR / 'data/raw/ratings.csv'}")
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == "__main__":
    load_ratings()
    
