#open the browser
from selenium import webdriver

browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#open amazon
print('Checking on amazon..............')
browser.get('https://www.amazon.in/Test-Exclusive-544/dp/B077PWK5BY/ref=sr_1_1?crid=3NZP8XAXMJPHG&dchild=1&keywords=oneplus+8+pro+mobile&qid=1597903131&sprefix=oneplus+%2Caps%2C397&sr=8-1')
#check price on amazon
ama=browser.find_element_by_id('priceblock_ourprice')
ap=ama.get_attribute('textContent')
ap=ap[2:]
pra=ap.split(',')
pra=float(''.join(pra))
print('Price on amazon: ')
print(pra)

#open flipkart
print('Checking on flipkart..............')
browser.get('https://www.flipkart.com/oneplus-8-pro-glacial-green-256-gb/p/itm4dcbd336cdd4f?pid=MOBFU897HFBWA7Y5&lid=LSTMOBFU897HFBWA7Y5J9QRBK&marketplace=FLIPKART&srno=s_1_10&otracker=AS_Query_OrganicAutoSuggest_4_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_8_na_na_na&fm=SEARCH&iid=bdba60c1-1efa-4ec3-b202-c08fed2d52cc.MOBFU897HFBWA7Y5.SEARCH&ppt=sp&ppn=sp&ssid=ttjtcafjkw0000001597903944834&qH=ea0a91036285d079')
#check price on flipkart
flp=browser.find_element_by_xpath('//div[@class="_1vC4OE _3qQ9m1"]')
fp=flp.get_attribute('textContent')
fp=fp[1:]
prf=fp.split(',')
prf=float(''.join(prf))
print('Price on flipkart: ')
print(prf)

#compare the price and make decision
if prf>pra:
	print('Go for Amazon')
elif pra>prf:
	print('Go for flipkart')
else:
	print('Same price. You can go anywhere you want')