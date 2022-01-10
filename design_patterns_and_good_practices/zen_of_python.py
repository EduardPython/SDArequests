import this
import codecs
import requests
import json

zen_of_python = codecs.encode(this.s, 'rot13')


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


print(translate(zen_of_python, target_lang="CS"))
