import re
#scraping bike name from html (wiht spaces, new lines, labels ) - "New"  'Neuron 7 WMN         New'"""

scraped_name = """New  Neuron 7 WMN      \n   New"""
def _normalize_name(raw_name):
    _name = re.sub("New", "", raw_name)
    formatted_name = _name.lstrip().rstrip().replace("\n", "")
    return formatted_name

#print(_normalize_name(scraped_name))

def new_normalize_name(raw_name):
    _name = re.sub("New", "", raw_name)
    formatted_name = _name.\
        lstrip().\
        rstrip().\
        replace("\n", "")
    return formatted_name

#print(new_normalize_name(scraped_name))

def new_normalize_name_v2(raw_name):
    name_without_new_string = re.sub("New", "", raw_name)
    name_without_new_line = name_without_new_string.replace("\n", "")
    name_without_spaces = name_without_new_line.strip()
    formatted_name = name_without_spaces
    return formatted_name

print(new_normalize_name_v2(scraped_name))