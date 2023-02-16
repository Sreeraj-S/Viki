import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer =WordNetLemmatizer()
intents = json.loads(open('data\chatdata\chat.json').read())

words = pickle.load(open('data\chatdata\words.pkl','rb'))
classes = pickle.load(open('data\chatdata\classes.pkl', 'rb'))
model =load_model('data\chatdata\chatbotmodel.h5')

intent_methods ={}

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return  sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    print('bag: ', bag)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1
    print('array: ', np.array(bag))
    return np.array(bag)

def predict_class(sentence):
    bow =bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda  x: x[1],reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intents':classes[r[0]], 'probability':str(r[1])})
    return return_list

def get_response(ints, intents_json):
    try:
        tag = ints[0]['intents']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag']  == tag:
                result = random.choice(i['response'])
                break
    except IndexError:
        result = "I don't understand!"
    return result


def request(message):
    ints = predict_class(message)

    if ints[0]['intents'] in intent_methods.keys():
        intent_methods[ints[0]['intent']]()
    else:
        return get_response(ints, intents)

if __name__ == '__main__':
    print('Chatbot is up and running!!!')
    while True:
        msg = input()
        print(request(msg))
