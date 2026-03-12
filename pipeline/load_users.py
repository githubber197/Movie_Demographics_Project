import pandas as pd
from faker import Faker
import random
from pipeline.load import get_connection

AGE_GROUPS = ["13-17","18-25", "26-35", "36-45", "46-60", "60+"]

def load_users():
    values = pd.read_csv("data/raw/ratings.csv")
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