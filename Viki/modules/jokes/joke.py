import requests


def jokes():
    res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"}
        )       
    if res.status_code == requests.codes.ok:
        joke = str(res.json()['joke'])
        return joke
    else:
        return 'oops!I ran out of jokes'

if __name__ == "__main__":
   print(jokes())
          