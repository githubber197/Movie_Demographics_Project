# 🎬 Demographics-Based Movie Analytics Dashboard

A data engineering project that analyzes **who watches what** — breaking down movie preferences by age group and country using the MovieLens 25M dataset.


---

## 📌 Project Overview

This project builds an end-to-end data pipeline that:
- Ingests 25 million ratings from the MovieLens dataset
- Enriches movie data with metadata from the OMDB API
- Generates mock user demographics (age group, country) using Faker
- Loads everything into a PostgreSQL database
- Visualizes insights on an interactive Streamlit dashboard

The goal is to answer questions like:
- Which genres does the 18–25 age group watch most?
- Which countries watch the most Action movies?
- Which age groups give the highest average ratings?

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data transformation |
| PostgreSQL | Data storage |
| psycopg2 | Python-Postgres connection |
| OMDB API | Movie metadata (title, genre, plot) |
| MovieLens 25M | Ratings dataset |
| Faker | Mock user demographics |
| Streamlit | Interactive dashboard |

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
          dashboard.py (Streamlit)
```

---

## 🗄️ Database Schema

- `users` — mock users with age group and country
- `movies` — movie titles and descriptions from OMDB
- `genres` — unique genre names
- `movie_genres` — many-to-many relationship between movies and genres
- `reviews` — ratings linked to users and movies

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
Run the schema in PostgreSQL:
```bash
psql -U your_db_user -d your_db_name -f database/schema.sql
```

### 5. Run the pipeline
```bash
# Load mock users
python pipeline/load_users.py

# Fetch movies from OMDB (1000/day limit)
python main.py

# Load ratings
python pipeline/load_ratings.py
```

### 6. Launch the dashboard
```bash
streamlit run dashboard.py
```

---

## 📊 Analytics Queries

Saved in `queries/demographics.sql`:

- **Genres by age group** — which genres each age group watches most
- **Countries by genre** — which countries watch a specific genre most
- **Average rating by age group** — how different age groups rate movies

---

## 📁 Project Structure

```
project/
├── data/
│   └── raw/              # MovieLens CSV files
├── database/
│   └── schema.sql        # PostgreSQL schema
├── pipeline/
│   ├── extract.py        # OMDB API fetching
│   ├── transform.py      # Data cleaning
│   ├── load.py           # DB insert functions
│   ├── load_users.py     # Mock user generation
│   ├── load_ratings.py   # Ratings pipeline
│   └── load_movielens.py # MovieLens links reader
├── queries/
│   ├── queries.py        # Python query functions
│   └── demographics.sql  # Raw SQL analytics queries
├── dashboard.py          # Streamlit dashboard
├── main.py               # Pipeline orchestrator
├── requirements.txt
└── .env                  # Not committed
```

---

## 🔮 Future Improvements

- Add Airflow for pipeline orchestration and scheduling
- Expand to real user data post-launch
- Add more demographic filters (gender, region)
- Deploy dashboard to Streamlit Cloud
