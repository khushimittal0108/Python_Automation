from selenium import webdriver
import time

#open google chrome
browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#open website accuweather
month=input('Enter the month:').lower()
year=input('Enter the year:')
url='https://www.accuweather.com/en/in/gurgaon/188408/'+month+'-weather/188408?year='+year+'&view=list'
browser.get(url)

#Collect Data from the website
high=browser.find_elements_by_class_name('high')
high_temp=[]
for i in high:
	j=i.get_attribute('textContent')
	high_temp.append(int(j[:2]))
#print(high_temp)

low=browser.find_elements_by_class_name('low')
low_temp=[]
for i in low:
	j=i.get_attribute('textContent')
	low_temp.append(int(j[3:5]))
#print(low_temp)


prec = browser.find_elements_by_xpath('//div[@class="info precip"]/p[2]')
precip=[]
for i in prec:
	j=i.get_attribute('textContent')
	precip.append(float(j[:2]))
#print(precip)

date=[]
for i in range(len(precip)):
	d=i+1
	date.append(d)
#print(date)

dic={'Date':date,'High Temperature':high_temp,'Low Temperature':low_temp,'Precipitation':precip}
#print(dic)

import pandas as pd
df=pd.DataFrame(dic)
#print(df)

df.to_csv('F:\\Education\\Alien Brains\\WeatherData.csv',index=False)
print('Done')

#Data Visualization using Colab