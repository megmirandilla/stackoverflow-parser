import urllib.request
import pprint
import copy
from bs4 import BeautifulSoup

data = {'question':'', 'answers':''}
question = {'desc':'', 'author':'', 'upvotes':'', 'comments':''}
answers_list = []
answer = {'desc':'', 'author':'', 'upvotes':'', 'comments':''}
comments_list = []
comment = {'desc':'', 'author':''}

url = 'https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists'
response = urllib.request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

#extracting question
question_title = soup.find("a",{"class":"question-hyperlink"}).text
question_body = soup.find("div",{"class":"question"})
qbody = question_body.find_all("p")

qb_list = []
for p in qbody:
	qb_list.append(p.text)

q_desc = question_title
for q in qb_list:
	q_desc += "\n" + q

author = question_body.find_all("div",{"class":"user-details"})
auth_list = []
for auth in author:
	auth_list.append(auth.find("a"))
if type(auth_list[0]) == 'NoneType':
	del auth_list[0]
q_author = auth_list.pop(0).text

q_upvotes = question_body.find("span").text

q_comm = question_body.find_all("div",{"class":"comment-body"})
for comm in q_comm:
	if type(comm) != 'NoneType':
		comment['desc'] = comm.find("span",{"class":"comment-copy"}).text
		comment['author'] = comm.find("a").text
		comments_list.append(copy.deepcopy(comment))

question['desc'] = q_desc
question['author'] = q_author
question['upvotes'] = q_upvotes
question['comments'] = copy.deepcopy(comments_list)

answer_blocks = soup.find_all("div",{"class":"answercell post-layout--right"})
for block in answer_blocks:
	if type(block) != 'NoneType':
		ans_p = block.find_all("p")
		ans_desc = ''
		for desc in ans_p:
			ans_desc += " " + desc.text
		answer['desc'] = ans_desc
		author = block.find_all("div",{"class":"user-details"})
		auth_list = []
		for auth in author:
			auth_list.append(auth.find("a"))
		if type(auth_list[0]) == 'NoneType':
			del auth_list[0]	
		answer['author'] = author.pop(0).text
		ans_upvotes = block.find_previous_sibling("div",{"class":"votecell post-layout--left"}).find("div",{"class":"vote"}).find("span").text
		answer['upvotes'] = ans_upvotes
		
		answers_list.append(copy.deepcopy(answer))

data['question'] = copy.deepcopy(question)
data['answers'] = copy.deepcopy(answers_list)
