# 🎬 Movie Demographics Dashboard

A data engineering project that explores **who watches what** — analyzing movie preferences across age groups and countries using the MovieLens 25M dataset.
---

## 📌 Project Overview

This project builds a full end-to-end data pipeline that:
- Ingests 25 million real ratings from the MovieLens dataset
- Enriches movie metadata from the OMDB API (title, genre, plot)
- Generates mock user demographics (age group, country) using Faker
- Loads everything into a PostgreSQL database
- Serves analytics via a FastAPI backend
- Visualizes insights on a custom HTML/CSS/JS dashboard with Chart.js

**Questions this project answers:**
- Which genres does the 18–25 age group watch most?
- Which countries watch the most Action movies?
- What are the highest rated movies by genre?
- Which movies have the most reviews?
- How do genre preferences vary across age groups? (heatmap)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data transformation |
| PostgreSQL | Data storage |
| psycopg2 | Python-Postgres connection |
| OMDB API | Movie metadata |
| MovieLens 25M | Ratings dataset |
| Faker | Mock user demographics |
| FastAPI | REST API backend |
| Chart.js | Interactive visualizations |
| APScheduler | Automated daily pipeline runs |

---

## 🏗️ Architecture

```
MovieLens CSVs          OMDB API
     │                     │
     ▼                     ▼
load_movielens.py      extract.py
     │                     │
     └──────────┬──────────┘
                ▼
          transform.py
                │
                ▼
            load.py  ←── load_users.py
                │         load_ratings.py
                ▼
          PostgreSQL DB
                │
                ▼
          queries/queries.py
                │
                ▼
            api.py (FastAPI)
                │
                ▼
          index.html (Chart.js Dashboard)
```

---

## 🗄️ Database Schema

- `users` — mock users with age group and country
- `movies` — movie titles and descriptions from OMDB
- `genres` — unique genre names
- `movie_genres` — many-to-many relationship between movies and genres
- `reviews` — ratings linked to users and movies

---

## 📊 Dashboard Features

| Chart | Description |
|-------|-------------|
| Genres by Age Group | Bar chart — which genres each age group watches most |
| Countries by Genre | Horizontal bar chart — top 10 countries per genre |
| Average Rating by Age Group | Bar chart — how each age group rates movies |
| Top Rated Movies by Genre | Table — highest rated movies per genre (10+ ratings) |
| Most Reviewed Movies | Table — movies with the most ratings overall |
| Genre/Age Heatmap | Heatmap — average ratings across all age groups and genres |

---

## 🗄️ Schema Design Decisions

**Why a separate `movie_genres` junction table?**
A single movie can belong to multiple genres (e.g. Action + Thriller). Storing genres directly in the movies table would violate normalization — instead we use a many-to-many junction table linking movies and genres.

**Why is `user_age` a VARCHAR instead of INT?**
Users are grouped into age ranges (e.g. "18-25") for demographic analysis. Storing ranges as strings is more meaningful than storing individual ages which would require grouping at query time.

**Why does `tmdb_id` have a UNIQUE constraint?**
Each movie has a unique IMDb ID — allowing duplicates would cause data collisions during inserts and return incorrect results during queries.

**Why ON DELETE CASCADE on reviews?**
If a user is deleted, their reviews should be deleted too. Without CASCADE, deleting a user would leave orphaned reviews pointing to a non-existent user, breaking referential integrity.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root:
```
OMDB_API_KEY=your_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### 4. Set up the database
```bash
psql -U your_db_user -d your_db_name -f database/schema.sql
```

### 5. Run the pipeline
```bash
# Load mock users
python pipeline/load_users.py

# Fetch movies from OMDB (1000 requests/day limit)
python main.py

# Load ratings
python pipeline/load_ratings.py
```

### 6. Start the API
```bash
uvicorn api:app --reload
```

### 7. Open the dashboard
Open `index.html` in your browser using a live server.

### 8. (Optional) Run the scheduler
Automatically fetches 1000 new movies every night at midnight:
```bash
python scheduler.py
```

---

## 📁 Project Structure

```
project/
├── data/
│   └── raw/                  # MovieLens CSV files
├── database/
│   └── schema.sql            # PostgreSQL schema
├── pipeline/
│   ├── extract.py            # OMDB API fetching with retry logic
│   ├── transform.py          # Data cleaning and validation
│   ├── load.py               # DB insert functions
│   ├── load_users.py         # Mock user generation with Faker
│   ├── load_ratings.py       # Ratings pipeline (vectorized)
│   └── load_movielens.py     # MovieLens links reader
├── queries/
│   ├── queries.py            # Python query functions
│   └── demographics.sql      # Raw SQL analytics queries
├── static/
│   ├── styles.css            # Dashboard styles
│   └── app.js                # Dashboard JavaScript
├── index.html                # Dashboard frontend
├── api.py                    # FastAPI backend
├── main.py                   # Pipeline orchestrator
├── scheduler.py              # Automated daily scheduler
├── requirements.txt
└── .env                      # Not committed
```

---

## 🔮 Future Improvements

- Deploy backend to Railway or Render
- Deploy frontend to Netlify or GitHub Pages
- Add Airflow for pipeline orchestration
- Expand to real user data post-launch
- Add more demographic filters (gender, region)
- Add movie search functionality
