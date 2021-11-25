import requests
from bs4 import BeautifulSoup
filmy_list = []
r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.text, "html.parser")
filmy = soup.find_all("td", class_="titleColumn")
for film in filmy:
    name = film.find("a").text
    year = film.find("span").text
    year = int(year.strip("()"))
    result = (name, year)
    filmy_list.append(result)

sorted_films = sorted(filmy_list, key=lambda x: x[1], reverse=True)
print(sorted_films)

#getting director director = film.find("a").get("title")