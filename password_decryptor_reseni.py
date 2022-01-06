import hashlib
import time


def vyndej_hashe():
    with open("hashed_passwords.txt", "r") as file:
        hashe = file.readlines()
    return hashe


def hash_word(word):
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    return hashed_word


def rozuzleni():
    start_time = time.time()
    res = []
    vyndany_hashe = vyndej_hashe()
    with open("list_of_all_english_words.txt", "r") as file:
        lines = file.readlines()
    for hash in vyndany_hashe:
        for word in lines:
            if hash.rstrip() == hash_word(word.rstrip()):
                res.append(word)
    print(f"Muj program trval {time.time() - start_time} ")
    return [i.rstrip() for i in res]    #hele zase kiwi :D


print(rozuzleni())