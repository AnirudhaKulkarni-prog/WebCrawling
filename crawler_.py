from bs4 import BeautifulSoup
import requests

with open("sample.html") as f_html:
	soup=BeautifulSoup(f_html,"lxml")

for article in soup.find_all('div',class_='article'):
	headline=article.h2.a.text
	print(headline)
	
	summary=article.p.text
	print(summary)









