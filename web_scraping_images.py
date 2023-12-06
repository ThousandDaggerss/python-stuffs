import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://freerangestock.com/popular_photos.php")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])

#  ------------------------------

htmldata = urlopen('https://freerangestock.com/popular_photos.php')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

for item in images:
    print(item['src'])
