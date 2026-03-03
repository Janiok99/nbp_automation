import requests
import pandas as pd

BASE_URL = "https://api.nbp.pl/api"

def get_eur_rate():
    """Pobiera aktualny kurs EUR z API NBP."""
    url = f"{BASE_URL}/exchangerates/rates/A/EUR/?format=json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    rate = data["rates"][0]["mid"]
    date = data["rates"][0]["effectiveDate"]

    return pd.DataFrame([{
        "data": date,
        "kurs_EUR": rate
    }])
