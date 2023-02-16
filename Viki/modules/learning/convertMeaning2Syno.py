import json

meaningSyn = {}


def loadJson():
    with open(r".\data\wordsdata\meaning.json",'r') as files:
        meaning = json.load(files) 
    return meaning

if __name__ == "__main__":
    meaning = loadJson()
    words = list(meaning.keys())
    for word in words:
        typeOfMeaning = meaning[word]
        for typeOf in list(typeOfMeaning.keys()):
            for meaNing in typeOfMeaning[typeOf]:
                words1 = []
                if meaNing not in list(meaningSyn.keys()):
                    for word1 in words:
                        if meaNing in meaning[word1][typeOf]:
                            words1.append(word1)
                meaningSyn[meaNing] = words1
            
