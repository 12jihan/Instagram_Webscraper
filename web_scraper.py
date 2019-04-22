from bs4 import BeautifulSoup

import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror

import requests
import json
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
        self.followers = 0
        self.following = 0
        self.posts = 0
        self.user_link = self.insta_url + self.user

    def search_user(self):
        self.req_url = ureq.urlopen(self.user_link).read()
        self.soup = BeautifulSoup(self.req_url, 'html.parser')
        self.data = self.soup.find_all('meta', attrs={'property': 'og:description'})
        self.text = self.data[0].get('content').split()
        

        self.username = self.text
        self.followers = self.text[0]
        self.following = int(self.__remCom__(self.text[2]))
        self.posts = int(self.__remCom__(self.text[4]))

        ##############################
        ##############################

        print('Data: ', self.text)
        print('\n*****************\n')
        print('Username: ', self.user)
        print('Followers: ', self.followers)
        print('Following: ', self.following)
        print('Posts: ', self.posts)

    def __remCom__(self, input):
        self.input = input.replace(',', '')
        return self.input