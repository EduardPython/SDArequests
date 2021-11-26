import requests
import re
from bs4 import BeautifulSoup

text = ""
r = requests.get("https://zdopravy.cz/airbus-ma-dalsi-velkou-zakazku-prvni-zakaznik-si-objednal-a350-v-nakladni-verzi-96785/")
soup = BeautifulSoup(r.text, "html.parser")
text_field = soup.find("div", {"id": "main-content"})
paragraphs = text_field.findChildren("p")
for p in paragraphs:
    text += p.text

pattern = "[AB]?[0-9]{3}[a-zA-Z]{1,3}"
letadla = re.findall(pattern, text)
print(set(letadla))








