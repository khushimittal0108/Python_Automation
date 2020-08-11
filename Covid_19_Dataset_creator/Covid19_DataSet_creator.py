#open google chrome
from selenium import webdriver
import time
import pandas as pd
import os

browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#open the website - worldometer
browser.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22")
time.sleep(20)


#Find where the data is stored
#retrieve the table
#create dataframe
covid = pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','Active Cases','Serious'])


#for each row in the table
for i in browser.find_elements_by_xpath("//*[@id='main_table_countries_today']/tbody/tr"):
	#find each element in the row
	td_list=i.find_elements_by_tag_name('td')
	row=[]
	#gather information 
	for td in td_list:
		row.append(td.text)
	#append to covid dataframe
	data={}
	for j in range(len(covid.columns)):
		data[covid.columns[j]]=row[j]
	
	covid= covid.append(data, ignore_index=True)


covid=covid[1:]
print(covid)

#store the data in the device
path='F:\\Education\\Alien Brains\\Covid19_Dataset.csv'
covid.to_csv(path,index=True)

print('The data has been stored at'+path)

#close the browser
browser.quit()



