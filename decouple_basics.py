import requests
import bs4
from decouple import config

api_key = config("api_key", default="")
username = config("username", default="")
password = config("password", default="")
heslo = config("heslo", default="heslo nenastaveno")


print(api_key)
print(username)
print(password)
print(heslo)