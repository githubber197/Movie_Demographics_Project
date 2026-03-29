from fastapi.middleware.cors import CORSMiddleware
import fastapi
from queries.queries import get_genres_by_age_group, get_countries_by_genre, get_avg_rating_by_age_group, get_top_movies_by_genre, get_most_reviewed_movies, get_genres_age_heatmap
from pipeline.load import get_connection

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/genres-by-age-group")
def read_genres_by_age_group(age_group: str):
    return get_genres_by_age_group(age_group).to_dict(orient="records")

@app.get("/countries-by-genre")
def read_countries_by_genre(genre: str):
    return get_countries_by_genre(genre).to_dict(orient="records")

@app.get("/avg-rating-by-age-group")
def read_avg_rating_by_age_group():
    return get_avg_rating_by_age_group().to_dict(orient="records")

@app.get("/top-movies-by-genre")
def read_top_movies_by_genre(genre: str):
    return get_top_movies_by_genre(genre).to_dict(orient="records")

@app.get("/most-reviewed-movies")
def read_most_reviewed_movies():
    return get_most_reviewed_movies().to_dict(orient="records")

@app.get("/genre-age-heatmap")
def read_genre_age_heatmap():
    return get_genres_age_heatmap().to_dict(orient="records")

@app.get("/stats")
def get_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            (SELECT COUNT(*) FROM movies) as total_movies,
            (SELECT COUNT(*) FROM users) as total_users,
            (SELECT COUNT(*) FROM reviews) as total_reviews,
            (SELECT COUNT(DISTINCT genre_id) FROM genres) as total_genres,
            (SELECT COUNT(DISTINCT movie_id) FROM movie_genres) as movies_with_genres
    """)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return {
        "total_movies": result[0],
        "total_users": result[1],
        "total_reviews": result[2],
        "total_genres": result[3],
        "movies_with_genres": result[4]
    }