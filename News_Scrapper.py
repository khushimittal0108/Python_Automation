#open the browser
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

#input the no. of pages
pages=int(input("Enter the no. of pages:"))

titles=[]
links=[]
#for each page
for i in range(1,pages+1):
	#get the url
	url='https://news.ycombinator.com/news?p='+str(i)
	
	#open the url
	r=urllib.request.urlopen(url)
	#source code
	c=r.read()
	#parsing the source code
	soup=BeautifulSoup(c,'html.parser')

	#gather the title and their links
	a=soup.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

	for j in a:
		title = j.text
		link=j.get('href')
		titles.append(title)
		links.append(link)


#store the data
dic={'news_title':titles,'URL':links}
df=pd.DataFrame(dic)
print(df)



