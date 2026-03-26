from fastapi.middleware.cors import CORSMiddleware
import fastapi
from queries.queries import get_genres_by_age_group, get_countries_by_genre, get_avg_rating_by_age_group

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