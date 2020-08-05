# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author: srakibul99
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on


import urllib.request
import urllib.error
import re
import sys


# Enter your function definitions here



def input(filename, topic):
   
        open, read, and decode the urls found in the file

        Parameters:

        filename (string) - input file that contains a list of the urls
        topic (string) - the word we are searching for

        Returns: null

    # build and return the dictionary for the given filename
    with open(filename, 'r', encoding='utf-8') as file:
        for url in file:
            try:
                # 'opens' the web page
                with urllib.request.urlopen(url) as url_file:
                    # reads the full contents of the decoded page
                    page = url_file.read().decode('UTF-8')
                    # search_text(page, url, topic)
            except urllib.error.URLError as url_err:
                    print('Error opening url: ', url, url_err)
            except UnicodeDecodeError as decode_err:
                print('Error decoding url: ', url)
                print(decode_err)
                continue
            else:
                search_text(page, url, topic)
                # print(url)
                # output(ref, url, topic)
                


def search_text(text, url, topic):

          search the web page for the topic

          Parameters:
          text (string) - web page, or the opened and read url
          url (string) - name of url, found from each line in the input file
          topic (string) - the word we are searching the web page for

          Returns: all_references (string) each instance the topic is mentioned

    all_references = ''
    # extract text containing the topic
    pattern = fr'>([^<]*\b{topic}\b.*?)<'
    matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
    if matches:
        all_references = '\n'.join(matches)
        output(all_references, url, topic)
    return all_references


def output(ref, url, topic):

          count the words found in the file

          Parameters:
          ref (string) - all of the references to the topic found in the page
          url (string) - name of url, found from each line in the input file
          topic (string) - the word we are searching the web page for

          Returns: out_file (file of strings) - in our working directory

    topic = topic + 'summary.txt'
    with open(topic, 'a', encoding='utf-8') as out_file:
        if ref:
            out_file.write('\n' + url)
            out_file.write('\n' + ref + '\n')
            out_file.write('-------------------------------------------------'
                           '-------------------------------')
    return out_file

def main():
    url = "https://www.google.com/maps/place/Target/@37.3249821,-121.9078608,11z/data=!4m8!1m2!2m1!1starget!3m4!1s0x808e3281ba49fde9:0xb19900ecafe5de4f!8m2!3d37.307352!4d-121.813394"
    try:
        # 'opens' the web page
        with urllib.request.urlopen(url) as url_file:
            # reads the full contents of the decoded page
            page = url_file.read().decode('UTF-8')
            # search_text(page, url, topic)
    except urllib.error.URLError as url_err:
        print('Error opening url: ', url, url_err)
    except UnicodeDecodeError as decode_err:
        print('Error decoding url: ', url)
        print(decode_err)
        # continue
    else:
        # search_text(page, url, topic)
        print(page)
        # output(ref, url, topic)


if __name__ == '__main__':
    main()


import re
import requests
from ast import literal_eval

urls = [
'https://www.google.com/maps?cid=15423079754231040967&hl=en',
'https://www.google.com/maps?cid=16168151796978303235&hl=en']

for url in urls:
    for g in re.findall(r'\[\\"http.*?\d+ reviews?.*?]', requests.get(url).text):
        data = literal_eval(g.replace('null', 'None').replace('\\"', '"'))
        print(bytes(data[0], 'utf-8').decode('unicode_escape'))
        print(data[1])


import json, requests

url_venues = 'https://api.foursquare.com/v2/venues/explore'
url_photos = 'https://api.foursquare.com/v2/venues/{}/photos'

CLIENT_ID = 'UNXKPYYYPY2PQFGNYL3KXWTKGNT20SO4ISO0YDROW0HORX2W'
CLIENT_SECRET = 'QWPXY050I0NWIEIGIGHGNUBM0XXWN42SNS2XGBGKL3RXBKP3'

'''
params = dict(client_id=CLIENT_ID,
              client_secret=CLIENT_SECRET,
              v='20200601',
              ll='40.7243,-74.0018',
              query='coffee',
              limit=1
              )

params_venues = dict(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     v='20200601',
                     near='San Jose, CA',
                     query='coffee',
                     limit=3
                     )

resp = requests.get(url=url_venues, params=params_venues)
data = json.loads(resp.text)


response - 2nd item of dict
groups is a list, so grab the 1st item (is a dict)
go to 'item' key in dict
get the 1st item (is a dict) - 'reasons', 'venue', etc.
get the 'venue' key

To get all venue keys in query, change ['items'][0] to  ['items'][0] for i in range(LIMIT)


id = data['response']['groups'][0]['items'][0]['venue']['id']
print(id)
url_photos_id = url_photos.format(id)
params_photos = dict(client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    v='20200601',
                    VENUE_ID=id)

resp_photos = requests.get(url=url_photos_id, params=params_photos)
data_photos = json.loads(resp_photos.text)

print(data_photos)
"""

