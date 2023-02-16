import requests


def jokes():
    res = requests.get('https://randomwordgenerator.com/',headers={"Accept":"application/json"}
        )       
    if res.status_code == requests.codes.ok:
        joke = res.json()
        return joke
    else:
        return 'oops!I ran out of jokes'

if __name__ == "__main__":
   print(jokes())