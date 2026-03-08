from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def load_movies(movies):
    conn = get_connection()
    cursor = conn.cursor()

    for movie in movies:
        cursor.execute("""
            INSERT INTO movies (movie_title, movie_description, tmdb_id)
            VALUES (%s, %s, %s)
            ON CONFLICT (tmdb_id) DO NOTHING
            RETURNING movie_id
        """, (movie['title'], movie['description'], movie['imdb_id']))

        result = cursor.fetchone()
        if result:
            movie_id = result[0]
            print(f"Inserted movie: {movie['title']} with ID: {movie_id}")

            for genre in movie['genre']:
                try:
                    cursor.execute("""
                        INSERT INTO genres (genre_name)
                        VALUES (%s)
                        ON CONFLICT (genre_name) DO NOTHING
                        RETURNING genre_id
                    """, (genre,))

                    genre_result = cursor.fetchone()
                    if genre_result:
                        genre_id = genre_result[0]

                        cursor.execute("""
                            INSERT INTO movie_genres (movie_id, genre_id)
                            VALUES (%s, %s)
                            ON CONFLICT DO NOTHING
                        """, (movie_id, genre_id))

                except Exception as e:
                    print(f"Error inserting genre {genre}: {e}")

    conn.commit()
    cursor.close()
    conn.close()
def get_existing_ids():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tmdb_id FROM movies")
    existing_ids = {row[0] for row in cursor.fetchall()}
    cursor.close()
    conn.close()
    return existing_ids
if __name__ == "__main__":
    test_conn = get_connection()
    print("Connection successful!")
    test_conn.close()