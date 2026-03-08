import time
from pipeline.extract import fetch_movie_details
from pipeline.transform import transform_movie_data
from pipeline.load import load_movies
from pipeline.load import load_movies, get_existing_ids

def read_movie_ids(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    imdb_ids = read_movie_ids("data/raw/movies_list.txt")
    
    existing_ids = get_existing_ids()
        
    transformed = []
    for imdb_id in imdb_ids:
        if imdb_id in existing_ids:
            print(f"Skipping {imdb_id} - already exists in database.")
            continue
        movie_list = fetch_movie_details(imdb_id)
        transformed.append(transform_movie_data(movie_list))
        time.sleep(0.5)
    
    load_movies(transformed)
    print("Pipeline complete!")
   