import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://stackoverflow.com/questions/50729310/trouble-fetching-a-link-from-a-dynamic-webpage')
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())

