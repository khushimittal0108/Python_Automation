from selenium import webdriver
import time
import pandas as pd
#open the browser
browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#go to twitter-explore-trending
browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(20)

#gather the hashtags
trend=[]
tags=browser.find_elements_by_tag_name('span')
for i in tags:
	a=i.get_attribute('textContent')
	if a.startswith('#') and a not in trend:
		trend.append(a)


#go to the tweets
urls=[]
for t in trend:
	url='https://twitter.com/search?q=%23'+t[1:]+'&src=trend_click'
	urls.append(url)

dic={'Hashtag':trend,'URL':urls}

df=pd.DataFrame(dic)
df.to_csv('F:\\Education\\Alien Brains\\Twitter_data.csv',index=False)
print('Data stored at F:\\Education\\Alien Brains\\Twitter_data.csv ')
