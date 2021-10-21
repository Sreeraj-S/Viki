import wikipedia

def wiki(data):
    response = wikipedia.summary(data, sentences=2)
    return response

if __name__ == "__main__":
    query = input("Enter the query: ")
    print(wiki(query))