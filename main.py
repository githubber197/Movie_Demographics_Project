import time
from pipeline.transform import transform_movie_data
from pipeline.load import load_movies, get_existing_ids
from pipeline.extract import fetch_with_retry
from pipeline.load_movielens import read_links


def run_pipeline():
    count = 0
    links = read_links()
    imdb_ids = links.values()
    existing_ids = get_existing_ids()
    transformed = []
    
    for imdb_id in imdb_ids:
        if imdb_id in existing_ids:
            print(f"Skipping {imdb_id} - already exists in database.")
            continue
        movie_list = fetch_with_retry(imdb_id)
        if movie_list is None:
            print(f"Failed to fetch {imdb_id} after all retries, skipping.")
            continue
        transformed.append(transform_movie_data(movie_list))
        time.sleep(0.5)
        count += 1
        if count == 1000:
            print("Stop limit reached of 1000 movies, ending pipeline.")
            break
            
    
    load_movies(transformed)
    print("Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()