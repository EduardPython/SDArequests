
from decouple import config


api_klic = config("api_key")
#username = config("username", default="")
#password = config("password", default="")
heslo = config("heslo", default="Heslo nenalezeno")


#print(api_klic)
#print(username)
#print(password)
print(heslo)