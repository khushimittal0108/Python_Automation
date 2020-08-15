from bs4 import BeautifulSoup
#to open url and get the page source
from urllib.request import urlopen

#page source
ps=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
soup = BeautifulSoup(ps,'html.parser')

body=soup.find('div',{'class':'ciPhotoContainer'})
head=soup.findAll('h3')

name=[]
for i in head:
	j=i.text
	name.append(j)

import pandas as pd 
columns=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=columns)


tr_list=soup.findAll('tr')

n=0
for i in tr_list:
	row=[]
	td_list=i.findAll('td')
	for j in td_list:
		row.append(j.text)
	dic={}
	try:
		for k in range(len(df.columns)):
			dic[df.columns[k]]=row[k]
		df=df.append(dic,ignore_index=True)
	except:
		df=pd.DataFrame( columns=columns)
		table_name=name[n]
		n=n+1
	df.to_csv('F:\\Education\\Alien Brains\\Team_rankings_ESPN_cricinfo\\'+table_name+'.csv',index=False)

print('Done')
	
