import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://codeforces.com/contest/1060/submission/44079628"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the div tags
tags = soup.findAll('div', attrs={'class':'file input-view'})
for tag in tags:
    print(tag.find('div', attrs={'class':'text'}).text, end = '')

i = 0
for tag in tags:
    if i <= 9:
        k = '0' + str(i)
    else:
        k = str(i)
    text = tag.find('div', attrs={'class':'text'}).text.strip()
    # j = 'input-' + j + '.txt'
    k = 'in' + k + '.txt'
    # read_hand = open(k, 'r')
    write_hand = open(k, 'w')
    # number = int(read_hand.read().strip())
    write_hand.write(str(text))
    # read_hand.close()
    write_hand.close()
    i += 1



url = "http://codeforces.com/contest/1060/submission/44079628"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the div tags
tags = soup.findAll('div', attrs={'class':'file output-view'})
for tag in tags:
     print(tag.find('div', attrs={'class':'text'}).text)

i = 0
for tag in tags:
    if i <= 9:
        k = '0' + str(i)
    else:
        k = str(i)
    text = tag.find('div', attrs={'class':'text'}).text.strip()
    # j = 'input-' + j + '.txt'
    k = 'out' + k + '.txt'
    # read_hand = open(k, 'r')
    write_hand = open(k, 'w')
    # number = int(read_hand.read().strip())
    write_hand.write(str(text))
    # read_hand.close()
    write_hand.close()
    i += 1
