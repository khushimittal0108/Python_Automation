from selenium import webdriver

user_id=input("Enter the email or phone number:")
password = input("Enter the password:")

#opening google chrome
browser=webdriver.Chrome("F:\\Education\\Alien Brains\\chromedriver.exe")

#opening facebook.com
browser.get('https://www.facebook.com')

#click on email or phone number
#look for input tag with specific id -- email
eop = browser.find_element_by_id("email")
#send email id or phone number to the email box
eop.send_keys(user_id)

#similarly for password
#click on password
passwd = browser.find_element_by_id("pass")
#send password to password box
passwd.send_keys(password)

#click on login button
#finding the button
login = browser.find_element_by_id('u_0_b')
#click on the button
login.click()

#close the browser
browser.quit()