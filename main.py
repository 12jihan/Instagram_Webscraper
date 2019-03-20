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

    def __init__(self, username, followers, following, posts):
        
        self.user = username
        self.followers = followers
        self.following = following
        self.posts = posts
        self.user_link = insta_url + user


    def inst_print_data(self):
        print(self.user)