import hashlib
import csv
def hash_word(word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    return(hashed_word)

# print(hash_word("jelen"))
# print(40*"-")
# print(hash_word("jelen"))
# print(40*"-")
# print(hash_word("Jelen"))
# print(40*"-")
# print(hash_word("Je1len"))


heslo = "nezlomitelneheslo"
ukradeny_hash = "214a69f3976044a3cf02d28c01c41298"
if hash_word(heslo) == ukradeny_hash:
    print("heslo prolomeno")
else:
    print("nespravne heslo")