SELECT COUNT(users.user_id), genres.genre_name FROM users JOIN reviews ON users.user_id = reviews.user_id JOIN movies ON reviews.movie_id = movies.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id WHERE users.user_age = '18-25' GROUP BY genres.genre_name ORDER BY COUNT(users.user_id) DESC;


SELECT COUNT(users.user_id), users.user_country FROM users JOIN reviews ON users.user_id = reviews.user_id JOIN movies ON reviews.movie_id = movies.movie_id JOIN movie_genres ON movies.movie_id = movie_genres.movie_id JOIN genres ON movie_genres.genre_id = genres.genre_id WHERE genres.genre_name = 'Action' GROUP BY users.user_country ORDER BY COUNT(users.user_id) DESC;


SELECT ROUND(AVG(reviews.movie_rating), 2) AS average_rating, users.user_age FROM reviews JOIN movies ON reviews.movie_id = movies.movie_id JOIN users ON reviews.user_id = users.user_id GROUP BY users.user_age ORDER BY average_rating DESC;