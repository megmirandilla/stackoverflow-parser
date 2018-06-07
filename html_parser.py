import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://stackoverflow.com/questions/50729310/trouble-fetching-a-link-from-a-dynamic-webpage')
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
# print(soup.get_text())

head_tag = soup.head
link_tag = soup.link

# print(head_tag.contents)

question_title = soup.find("a",{"class":"question-hyperlink"}).text
question_body = soup.find("div",{"class":"question"}).find("p").text
question = [question_title,question_body]
print(question)



# for obj in question:
# 	print(obj)