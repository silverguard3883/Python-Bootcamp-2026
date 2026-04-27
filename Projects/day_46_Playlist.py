from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

top_100_songs = []

for row in soup.find_all("div", class_="o-chart-results-list-row-container"):
    title_tag = row.find("h3")

    if title_tag:
        song_title = title_tag.get_text(strip=True)
        top_100_songs.append(song_title)

for i, song in enumerate(top_100_songs, start=1):
    print(f"{i}. {song}")