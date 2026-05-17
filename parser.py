import requests
from bs4 import BeautifulSoup

URL = "https://countrymeters.info/ru/World"

def get_page():
    response = requests.get(URL) = requests.get(URL)

    if response.status_code == 200:
        return response.text

    return None

def parse_birth_data(html):
    soup = BeautifulSoup(html, "html.parser")

    stats = soup.find_all("div", {"class": "counter"})

    result = []

    for item in stats[:5]:
        title = item.find("div", class_="counter_title")
        value = item.find("span", class_="counter_number")

        if title and value:
            result.append({
                "title": title.text.strip(),
                "value": value.text.strip()
            })

    return result