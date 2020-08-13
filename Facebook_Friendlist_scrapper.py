from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

#login to facebook
user_id=input("Enter the email or phone number:")
password = input("Enter the password:")

browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")
browser.get('https://www.facebook.com/')


eop = browser.find_element_by_id("email")
eop.send_keys(user_id)

passwd = browser.find_element_by_id("pass")
passwd.send_keys(password)

login = browser.find_element_by_id('u_0_b')
login.click()
time.sleep(60)

#Go to your profile
profile=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
profile.click()
#click on friends
time.sleep(10)
friend = browser.find_element_by_xpath('//*[@class="bp9cbjyn j83agx80 btwxx1t3 k4urcfbm"]/a[3]')
friend.click()

time.sleep(10)

#scroll to load the list
while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	try:
		exit_control=browser.find_element_by_xpath("//*[contains(text(), 'Questions')]")
		break
	except:
		continue

print('done')

#using beautiful soup parse the page source
ps=browser.page_source
soup = BeautifulSoup(ps,'html.parser')

#gather the data
flist=soup.find('div',{'class':'i1fnvgqd lhclo0ds btwxx1t3 j83agx80'})
friends=[]
for i in flist.findAll('a'):
	friends.append(i.text)

#clean the data
names_list=[]
for name in friends:
    if(name=='FriendFriends'):
        continue
    if('friends' in name):
        continue
    if(name==''):
        continue
    else:
        names_list.append(name)

#print the friend list
print(names_list)
print('Total Friends :')
print(len(names_list))

#close the browser
browser.quit()