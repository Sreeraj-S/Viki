import json
from PyDictionary import PyDictionary

dics = PyDictionary()

def getMeaning(word,meaning):
    get_meaning = dics.meaning(word)
    return get_meaning

if __name__ == "__main__":
    open with()