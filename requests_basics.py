import requests


#requests.get("https://www.imdb.com/chart/top/")
#response = requests.get("https://www.imdb.com/chart/top/")
#print(response)
#print(response.status_code)
#print(response.text)
#print(response.json())

#regiojet_lokace_z_api = requests.get("https://brn-ybus-pubapi.sa.cz/restapi/consts/locations")
#regiojet_lokace = regiojet_lokace_z_api.json()

#for country in regiojet_lokace:
#    print(country["country"])

yoda = requests.get("https://api.funtranslations.com/translate/yoda.json?text=Master%20Obiwan%20has%20lost%20a%20planet.")
# link https://www.theguardian.com/world/2011/apr/13/czech-president-steals-pen
text = "As Piñera addresses journalists and gives Klaus an enthusiastic welcome, the Czech president takes the pen out, examines it carefully, moves his hands under the table, shuffles with his jacket, then buttons it up with both hands and finally lets his empty hands emerge above the table again to close the case."
yoda_speak = requests.get(f"https://api.funtranslations.com/translate/yoda.json?text={text}")
print(type(yoda_speak.json()))

url = "https://api.funtranslations.com/translate/yoda.json?"
parametry = {"text" : text}
yoda_1 = requests.get(url=url, params=parametry)
response = yoda_1.json()