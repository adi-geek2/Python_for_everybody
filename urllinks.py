# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#User input
url = input('Enter - ')
count = int(input('Enter count as an integer :'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retrieving: " + url)

list_of_tags = list()

# Retrieve all of the anchor tags
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    list_of_tags.append((tag.get('href', None)))

for iter in range(1,count):
    html = urllib.request.urlopen(list_of_tags[position], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving: " + list_of_tags[position])
    list_of_tags.clear()
    # Retrieve all of the anchor tags
    tags_new = soup('a')
    for tag_new in tags_new:
        #print(tag.get('href', None))
        list_of_tags.append(tag_new.get('href', None))
print(list_of_tags[position])