import urllib.request
response = urllib.request.urlopen('https://stackoverflow.com/questions/7735866/how-to-create-soap-client')
html = response.read()

print(html)