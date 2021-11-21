import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.text, "html.parser")
filmy = soup.find_all("td", class_="titleColumn")
for film in filmy:
    name = film.find("a").text
    print(name)