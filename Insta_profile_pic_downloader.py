#open google chrome
from selenium import webdriver
browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#input the profile name
user_id=input("Enter the profile:")

#open the instagram profile
url='https://www.instagram.com/'+user_id
browser.get(url)

#Download the pic
try:
	#public profile
	image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
	#for private accounts
	image=browser.find_element_by_xpath('//img[@class="be6sR"]')
print("done")

img_link=image.get_attribute('src')

#download image using link
path='F:\\Education\\Alien Brains\\'+user_id+'.jpg'
import urllib.request
urllib.request.urlretrieve(img_link,path)

print("the profile pic is downloaded at:"+path)





