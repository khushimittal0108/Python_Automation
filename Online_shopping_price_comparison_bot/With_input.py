#take price from a website
from selenium import webdriver
import smtplib
import schedule

def amazonprice():
	browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")
	print('Checking on amazon..............')
	browser.get('https://www.amazon.in/Test-Exclusive-544/dp/B077PWK5BY/ref=sr_1_1?crid=3NZP8XAXMJPHG&dchild=1&keywords=oneplus+8+pro+mobile&qid=1597903131&sprefix=oneplus+%2Caps%2C397&sr=8-1')
	ama=browser.find_element_by_id('priceblock_ourprice')
	ap=ama.get_attribute('textContent')
	ap=ap[2:]
	pra=ap.split(',')
	pra=float(''.join(pra))
	return pra

def Mailll():
	#when discovered low, get info by mail
	#connect to gmail
	s=smtplib.SMTP('smtp.gmail.com',587)
	#make connection secure
	s.starttls()
	#log in 
	mail=input('Enter your Mail id:')
	passwd=input('Enter your password:')
	s.login(mail,passwd)
	#mail the concerned person
	c_mail=input('Enter the mail of reciever:')
	s.sendmail(mail,c_mail,'Hurry up! The price is low. Grab the deal.')
	#quit the connection
	s.quit()
	

#compare discovered price with your price
def task():
	p= int(input('Desired Price:'))
	a=amazonprice()
	if a<=p:
		Mailll()
		print('Mail Sent')
	else:
		print("Don't Buy")

#perforn a task repeatedly 
schedule.every().day.at("18:00").do(task)
#schedule.every(30).seconds.do(task)
print('getting inside while loop')
#creating infinite loop to run
while True:
	schedule.run_pending()


