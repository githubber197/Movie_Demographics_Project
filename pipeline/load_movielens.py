from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent

def read_links(file_path=BASE_DIR / "data/raw/links.csv"):
    df = pd.read_csv(file_path, dtype={"movieId": "int32", "imdbId": "str", "tmdbId": "float32"})
    df["imdbId"] = "tt" + df["imdbId"].str.zfill(7)
    return dict(zip(df["movieId"], df["imdbId"]))

if __name__ == "__main__":
    links = read_links()
    print(f"Total links: {len(links)}")
    print(list(links.items())[:5])