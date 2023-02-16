import pickle

with open(r'.\data\wordsdata\words.pkl','rb') as files:
    loadWords = pickle.load(files)
    print(len(loadWords))
    print(loadWords[2])
# with open(r'.\data\wordsdata\words.pkl','wb') as files:
#     loadWords = loadWords[:3261]
#     pickle.dump(loadWords,files)