from PyDictionary import PyDictionary
import json
import pickle
import threading
import time

meaning ={}
dictionary = PyDictionary()

def getMeaning(word,meaning):
    get_meaning = dictionary.meaning(word)
    print(get_meaning)
    if get_meaning != None:
        meaning[word]  = get_meaning
        print("found")
    return meaning

def dumpJson(dictMeaning):
        with open(r".\data\wordsdata\meaning.json",'w') as files:
            json.dump(dictMeaning,files)

def loadJson():
        with open(r".\data\wordsdata\meaning.json",'r') as files:
            meaning = json.load(files) 
        return meaning

def loadData():
    with open(r'.\data\wordsdata\words.pkl','rb') as files:
        loadWords = pickle.load(files)
    return loadWords

def mainWord2Dic():
    loadWords = loadData()
    for word in loadWords:
        print(word)
        try:
            meaning = loadJson()
        except Exception as e:
            print(e)
        meaningDic_keys = list(meaning.keys())
        if word not in meaningDic_keys:
            meaning = getMeaning(word,meaning)
            dumpJson(meaning)
    

if __name__ == '__main__':
    i=0
    while True:
        print(i)
        mainWord2Dic()
        time.sleep(1000)
        i+=1