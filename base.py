import base64
client_id = "1c774acbfa6faec3a5cC131X8"
client_secret = "c1d4fcbfa6faec3a5c0b84aec2f5e98f"
encodedData = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
authorization_header_string = f"Authorization: Basic {encodedData}"

print(authorization_header_string)
#Tiket Sandbox API

#username : kiwi.com
#password : gu)pUK3G(EWUe79#
#{
#"clientId" : "1c774acbfa6faec3a5cC131X8",
#"clientSecret" : "c1d4fcbfa6faec3a5c0b84aec2f5e98f",
#"storeId" : "TIKETCOMB2B",
#"channelId" : "KIWI.COM",
#"resellerId" : "34571449",
#"resellerType" : "B2B"
#}