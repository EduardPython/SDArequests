import requests
import csv
from bs4 import BeautifulSoup
filmy_list = []
r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.text, "html.parser")
filmy = soup.find_all("td", class_="titleColumn")

for film in filmy:
    name = film.find("a").text
    year = film.find("span").text
    year_int = int(year.strip("()"))

    reziser_a_herci = [film.find("a").get("title").split(",")[0].strip(" (dir.)")] + [
        film.find("a").get("title").split(",")[1:]]
    jmeno_rok_rez_herci = [name, year_int, reziser_a_herci]
    filmy_list.append(jmeno_rok_rez_herci)
    sorted_filmy = sorted(filmy_list, reverse=True, key=lambda x: x[1])
print(sorted_filmy)

#headers = ["jmeno_filmu", "rok", "reziser", "herci"]
#sorted_filmy #struktura ['Duna', 2021, 'Denis Villeneuve, ["Timothée Chalamet", "Rebecca Ferguson"]]

# --> ulozit do csv --> imdb_top250.csv