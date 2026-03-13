import pandas as pd
from faker import Faker
import random
from load import get_connection
from pathlib import Path

AGE_GROUPS = ["13-17","18-25", "26-35", "36-45", "46-60", "60+"]
BASE_DIR = Path(__file__).parent.parent

def load_users():
    values = pd.read_csv(BASE_DIR / "data/raw/ratings.csv", usecols=["userId"])
    fake = Faker()
    conn = get_connection()
    cursor = conn.cursor()
    for user_id in values["userId"].unique():
        
        name = fake.name()
        age_group = random.choice(AGE_GROUPS)
        country = fake.country()
        cursor.execute(
        "INSERT INTO users (user_name, user_age, user_country) VALUES (%s, %s, %s)",
        (name, age_group, country)
        )
        
    
    
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == "__main__":
    load_users()
    print(f"Users loaded successfully from {BASE_DIR / 'data/raw/ratings.csv'}")
    
