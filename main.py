import time
from pipeline.extract import fetch_movie_details
from pipeline.transform import transform_movie_data
from pipeline.load import load_movies

def read_movie_ids(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    imdb_ids = read_movie_ids("data/raw/movies_list.txt")
    
    transformed = []
    for imdb_id in imdb_ids:
        movie_list = fetch_movie_details(imdb_id)
        transformed.append(transform_movie_data(movie_list))
        time.sleep(0.5)
    
    load_movies(transformed)
    print("Pipeline complete!")