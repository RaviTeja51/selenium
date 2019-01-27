'''This scripit login into your flickr account and opens up the requested image'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

'''Specify the path of the chromedriver'''

#creates an object for the Chrome
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


#.get()opens up the webpage on chrome extension
driver.get("https://www.flickr.com/signin")


#To search for an html element making use of the element name
name = driver.find_element_by_name("username")
usr = input("Enter your mail-id for flickr, if not registered run python3 image.py:")


#sends the mail-id and also hits enter(Keys.RETURN is  equivalent to enter on keyboard)
name.send_keys(usr,Keys.RETURN)


#waits for 30 seconds so that the browser loadsup the html page
driver.implicitly_wait(30)
pwd = getpass("Enter your account password:")


#seaarches for the element with name "password"
password = driver.find_element_by_name("password")
password.send_keys(pwd,Keys.RETURN)

#waits for 30 seconds
driver.implicitly_wait(30)


image = input("Enter the discription of the image: ")
search = driver.find_element_by_id("search-field")
search.send_keys(image,Keys.RETURN)
