from decouple import config
import requests

api_key = config("deepl_api_key")
url = config("deepl_url")


def translate(text, target_lang, source_lang=None):
    params = {
        "auth_key": api_key,
        "text": text,
        "target_lang": target_lang
    }
    if source_lang:
        params.update({"source_lang": source_lang})
    response = requests.post(url=url, params=params)
    # translation = response.json()["translations][0]["text]
    translation = response.json().get("translations")[0].get("text")
    return translation


#text = "As Piñera addresses journalists and gives Klaus an enthusiastic welcome, the Czech president takes the pen out, examines it carefully, moves his hands under the table, shuffles with his jacket, then buttons it up with both hands and finally lets his empty hands emerge above the table again to close the case."
#prelozit_do = "CS"
#print(translate(text, prelozit_do))

def translator():
    input_text = input("zadejte text pro prelozeni: ")
    prelozit_do = input("do jakého jazyka chcete prelozit: ")
    return translate(input_text, prelozit_do)

print(translator())
#if __name__ == "__main__":
#    translator()

