import requests
import webbrowser
import sys, re, goslate
from bs4 import BeautifulSoup

def _get_soup_object(url, parser="html.parser"):
    return BeautifulSoup(requests.get(url).text, parser)

try:
   # term = input("Term:")
    url = "https://www.oxfordlearnersdictionaries.com/definition/english/hi?q=hi"
    webbrowser.open(url)
    # html = _get_soup_object("https://www.oxfordlearnersdictionaries.com/definition/english/{0}?q={0}".format(term))
    # print(html)
except Exception as e:
    print("Error: The Following Error occured: %s" % e)

