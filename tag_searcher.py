from bs4 import BeautifulSoup
import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror
import json
import ssl
import re
import io

import web_scraper as ws


inputTag = input('Enter in a tag: ')
hash_tag = inputTag
test = ws
x = ureq.urlopen('https://www.instagram.com/explore/tags/' + hash_tag).read()
soup = BeautifulSoup(x, 'html.parser')
data = str(soup)
# text = data[0].get('content').split()
print('\n##################################################\n')

# to include usernames with '.' in the name :  r'((?<=@)\w+\.\w+)'
re_object = re.findall(r'((?<=@)\w+)', data, re.M|re.I )

re_objectArr = re_object

print(str(len(re_object)) + ' Users in the list')

for i in re_object:
    print(i)
    print('########')
    test = ws.Insta_Scrape(i)
    test.search_user()
# print('writing file...')

# # opens file to read and sets the permission to 'w' or write
# f = open('test.json', 'w')
# # response to write string data to the document specified
# f.write(str(re_object))

print('done!')