import requests
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#scraping input files
url = "http://codeforces.com/contest/1060/submission/44079628"
html=''
for i in range(0,10): #if unsuccessful, try for 10 times
    html=requests.get(url,timeout=5)
    if html.status_code==200:
        break
# print(html.status_code)
if html.status_code ==200:
    soup = BeautifulSoup(html.text, 'lxml')
    # print(soup)

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
else:
    print("failed to get input files")


#scraping ouput files
url = "http://codeforces.com/contest/1060/submission/44079628"
html=''
for i in range(0,10): #if unsuccessful, try for 10 times
    html=requests.get(url,timeout=5)
    if html.status_code==200:
        break
# print(html.status_code)
if html.status_code ==200:
    soup = BeautifulSoup(html.text, 'lxml')
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
else:
    print("Failed to get ouput files")
