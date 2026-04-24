from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

top_100 = []

for tag in soup.find_all(name="h3", class_="title"):
    top_100.append(tag.text)

top_100 = top_100[::-1]

with open("top_100.txt", "w") as file:
    for item in top_100:
        file.write(f"{item}\n")