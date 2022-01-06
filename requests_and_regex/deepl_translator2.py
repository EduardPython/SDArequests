import requests
import json
import smtplib
from email.message import EmailMessage

deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
deepl_url = "https://api-free.deepl.com/v2/translate"

text = "As Piñera addresses journalists and gives Klaus an enthusiastic welcome, the Czech president takes the pen out, examines it carefully, moves his hands under the table, shuffles with his jacket, then buttons it up with both hands and finally lets his empty hands emerge above the table again to close the case."


def translate(text, target_lang, source_lang=None):
    deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
    deepl_url = "https://api-free.deepl.com/v2/translate"
    parametry = {
        "auth_key": deepl_api_key,
        "text": text,
        "target_lang": target_lang
    }
    if source_lang:
        parametry.update({"source_lang": source_lang})

    preklad = requests.get(url=deepl_url, params=parametry).json()
    return preklad["translations"][0]["text"]


# print(translate("kiwi neni zelenina", "EN", "CS"))

def send_email(reciever_email, message):
    sender_email = "rebelbean@seznam.cz"
    receiver_email = [reciever_email]  # recipients
    password = "passwordtest"
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Preklad'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP_SSL('smtp.seznam.cz', 465)  # choose your provider server
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    return "Email sent!"


def translator():
    text = input("Zadaj text, ktorý chceš preložiť: ")
    tar_language = input("Do jakeho jazyka to chcete prelozit: ")
    preklad = translate(text, tar_language)
    na_mail = input("chcete poslat preklad na mail? yes/no: ")
    if na_mail == "yes":
        poslat_na_mail = input("zadejte email: ")
        send_email(poslat_na_mail, preklad)
    return preklad

# print(translator())
