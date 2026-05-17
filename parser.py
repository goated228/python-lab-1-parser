import requests
from bs4 import BeautifulSoup

URL = "https://countrymeters.info/ru/World"

def get_page():
    response = requests.get(URL) = requests.get(URL)

    if response.status_code == 200:
        return response.text

    return None
