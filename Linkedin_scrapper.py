from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#open the browser
user_id=input("Enter the email or phone number:")
password = input("Enter the password:")

browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#go to sign in page
browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

#login to the accounts
si=browser.find_element_by_xpath('//a[@class="main__sign-in-link"]')
si.click()

em=browser.find_element_by_id("username")
em.send_keys(user_id)

pw=browser.find_element_by_id("password")
pw.send_keys(password)

but=browser.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')
but.click()

'''
#scroll to load all the frinds
while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	try:
		exit_control=browser.find_element_by_xpath("//*[contains(text(), name_of_last_connection)]")
		break
	except:
		continue
'''

#Gather all the connections
pg=browser.page_source
soup=BeautifulSoup(pg,'html.parser')
conn=soup.findAll('div',{'class':'mn-connection-card__details'})

connections=[]
for i in conn:
	a=i.find('a')
	link=a.get('href')
	connections.append(link)


#for each connection store name, current position and contact info
cname=[]
cposition=[]
ccontact=[]
for i in connections:
	url='https://www.linkedin.com'+i
	browser.get(url)
	na=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/ul[1]/li[1]')
	name=na.text
	cname.append(name)
	cpa=browser.find_element_by_xpath('//div[@class="flex-1 mr5"]/h2[1]')
	position=cpa.text
	cposition.append(position)
	contact=url+'detail/contact-info/'
	ccontact.append(contact)

#store data in csv file
dic={'Name':cname,'Current position':cposition,'Contact info':ccontact}
df=pd.DataFrame(dic)
df.to_csv('F:\\Education\\Alien Brains\\Linkedin_Scrapper\\connections.csv',index=False)
print('Done')
