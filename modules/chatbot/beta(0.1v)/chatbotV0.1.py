from PyDictionary import PyDictionary
import json
dictionary = PyDictionary()
words = []
sentence = input("Sentence:")



def get_grammar(line):
    words = line.split()
    grammar_format = []
    get_meaning = {}
    print(words)
    for word in words:
        print("\n")  
        if word.isdigit():
            grammar_format.append("no")
            continue
        print(word)
        get_meaning = dictionary.meaning(word.lower())
        if get_meaning == None :
            grammar_format.append('none')
            continue
        print(get_meaning)
        key = list(get_meaning.keys())
        for x in grammar_format:
            if x in key:
                key.remove(x)
        print(key)
        if len(key)==1:
            grammar_format.append(key[0])
            continue
        lstIndex = len(grammar_format)-1
        if lstIndex != -1 and grammar_format[lstIndex] == 'Noun':
            grammar_format.append(key[0])
            continue
        else:
            grammar_format.append(key[0])
    print("\n")    
    print(words)
    print(grammar_format)

if __name__ == '__main__':
    get_grammar(sentence)