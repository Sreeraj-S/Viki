import os
import configparser
import webbrowser
from googleapiclient.discovery import build

config = configparser.RawConfigParser()
config.read('.\data\localdata\secret.cfg', 'utf-8')
api_key = config['youtubeauth']['secret']
youtube = build('youtube', 'v3', developerKey=api_key)
def searchVideoID(query):
    request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=query
        )
    response = request.execute()
    return response['items'][0]['id']['videoId']
def openVideo(videoID):
    webbrowser.open(f'https://www.youtube.com/watch?v={videoID}')

if __name__ == "__main__":
    #print(searchVideoID('end of times by alan walker'))
    query = input('Enter the video to search: ')
    webbrowser.open(f'https://www.youtube.com/watch?v={searchVideoID(query)}')