from bs4 import BeautifulSoup
import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror
import requests
import json
import ssl
import re

# user = "demig.od"
# x = ureq.urlopen('https://www.instagram.com/'+user).read()
# soup = BeautifulSoup(x, 'html.parser')
# data = soup.find_all('meta', attrs={'property': 'og:description'})
# text = data[0].get('content').split()

# username = '@'+user
# followers = text[0]
# following = text[2]
# posts = text[4]


# print('Data: ', text)
# print('\n*****************\n')
# print('Username: ', username)
# print('Followers: ', followers)
# print('Following: ', following)
# print('Posts: ', posts)

class Insta_Scrape:

    insta_url = 'https://www.instagram.com/'

    # constructor for defining the instance variables
    def __init__(self, username):
        self.user = username
        self.followers = none
        self.following = none
        self.posts = none
        self.user_link = insta_url + user


    def search_user(self):
        self.req_url = ureq.urlopen(self.user_link).read()
        self.soup = BeautifulSoup(req_url, 'html.parser')
        self.data = soup.find_all('meta', attrs={'property': 'og:description'})
        self.text = data[0].get('content').split()

test = Insta_Scrape("Demig.od")

test.search_user()