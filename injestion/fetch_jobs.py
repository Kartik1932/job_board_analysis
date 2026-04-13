import requests
import json
from datetime import datetime
import os

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY=os.getenv("ADZUNA_APP_KEY")

def fetch_jobs(page=1):
    url=f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,
        "what": "software engineer"
    }

    response = requests.get(url, params=params)
    return response.json()

def save_raw(data):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"data/raw/jobs_{ts}.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    data = fetch_jobs()
    save_raw(data)