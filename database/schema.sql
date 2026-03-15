CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    user_age VARCHAR(10),
    user_country VARCHAR(255) NOT NULL
);

CREATE TABLE movies(
    movie_id SERIAL PRIMARY KEY,
    tmdb_id VARCHAR(20) UNIQUE NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    movie_description TEXT
);

CREATE TABLE reviews(
    review_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    movie_id INT NOT NULL REFERENCES movies(movie_id) ON DELETE CASCADE,
    movie_rating DECIMAL(4, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE genres(
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE movie_genres(
    movie_id INT NOT NULL REFERENCES movies(movie_id) ON DELETE CASCADE,
    genre_id INT NOT NULL REFERENCES genres(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, genre_id)
);

