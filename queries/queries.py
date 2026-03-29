from pipeline.load import get_connection
import pandas as pd

def get_genres_by_age_group(age_group):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT COUNT(users.user_id), genres.genre_name FROM users JOIN reviews ON users.user_id = reviews.user_id JOIN movies ON reviews.movie_id = movies.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id WHERE users.user_age = %s GROUP BY genres.genre_name ORDER BY COUNT(users.user_id) DESC;
                   """,(age_group,))
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["count", "genre"])
    cursor.close()
    conn.close()
    return df
def get_countries_by_genre(genre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT COUNT(users.user_id), users.user_country FROM users JOIN reviews ON users.user_id = reviews.user_id JOIN movies ON reviews.movie_id = movies.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id WHERE genres.genre_name = %s GROUP BY users.user_country ORDER BY COUNT(users.user_id) DESC LIMIT 10;

                     """,(genre,))
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["count", "country"])
    cursor.close()
    conn.close()
    return df
def get_avg_rating_by_age_group():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT ROUND(AVG(reviews.movie_rating), 2) AS average_rating, users.user_age FROM reviews JOIN movies ON reviews.movie_id = movies.movie_id JOIN users ON reviews.user_id = users.user_id GROUP BY users.user_age ORDER BY average_rating DESC;
                    """)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["average_rating", "age_group"])
    cursor.close()
    conn.close()
    return df

def get_top_movies_by_genre(genre):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT movies.movie_title, ROUND(AVG(reviews.movie_rating), 2) AS average_rating FROM movies JOIN reviews ON movies.movie_id = reviews.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id WHERE genres.genre_name = %s GROUP BY movies.movie_title HAVING COUNT(reviews.movie_rating) > 10 ORDER BY average_rating DESC LIMIT 10;
                    """,(genre,))
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["movie_title", "average_rating"])
    cursor.close()
    conn.close()
    return df

def get_most_reviewed_movies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT movies.movie_title, COUNT(reviews.review_id) AS review_count FROM movies JOIN reviews ON movies.movie_id = reviews.movie_id GROUP BY movies.movie_title ORDER BY review_count DESC LIMIT 10;
                    """)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["movie_title", "review_count"])
    cursor.close()
    conn.close()
    return df

def get_genres_age_heatmap():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT users.user_age, genres.genre_name, ROUND(AVG(reviews.movie_rating), 2) AS average_rating FROM users JOIN reviews ON users.user_id = reviews.user_id JOIN movies ON reviews.movie_id = movies.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id GROUP BY users.user_age, genres.genre_name;
                    """)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=["age_group", "genre", "average_rating"])
    cursor.close()
    conn.close()
    return df
