import requests
from bs4 import BeautifulSoup

URL = "https://countrymeters.info/ru/World"


def get_page():
    response = requests.get(URL)

    if response.status_code == 200:
        return response.text

    return None


def parse_birth_data(html):
    soup = BeautifulSoup(html, "html.parser")

    counter_stats = soup.find_all("td", {"class": "counter"})
    name_stats = soup.find_all("td", {"class": "data_name"})

    result = []

    for name, counter in zip(name_stats[:10], counter_stats[:10]):
        name_text = name.get_text(strip=True)
        counter_text = counter.get_text(strip=True)
        if name_text and counter_text:
            result.append({
                "title": name_text,
                "value": counter_text
            })

    return result
