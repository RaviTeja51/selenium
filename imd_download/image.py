'''This scripit opens flickr and creates an acount'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



'''Creates an object for Chrome'''
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

'''open flickr on chrome extendion'''
driver.get("https://www.flickr.com/signup")

#send_keys() sends the text and key words like Enter etc.

#Searches for a html element with class name ureg-fname and ureg-lname.
fname = driver.find_element_by_class_name('ureg-fname')
lname = driver.find_element_by_class_name('ureg-lname')


#Clears the text field
fname.clear()
lname.clear()
first = input("Enter your first name:")


#send the input user name to the html text field
fname.send_keys(first)
sur = input("\nEnter your surname")
#sends surname to surname field in sing-up form
lname.send_keys(sur)


#Finds html element with name "email"
email = driver.find_element_by_name("email")
mail = input("\nEnter your mail, it can be any valid email address")
#send email to email field
email.send_keys(mail)

#Finds html element with name "password"
password = driver.find_element_by_name("password")
pwd = input("\nChoose your password:")
password.send_keys(pwd)

#Finds html element with id "usernamereg-month".
#Select() is a class which provides methods for interacting drop down.
month = Select(driver.find_element_by_id('usernamereg-month'))
birth = input("\nEnter your birth month")
#select_by_value() method selcets an option with value which is provided as argument, there are other methods like select_by_name etc
month.select_by_value(birth)


#Finds element with name "dd"
date_ = input("Enter your birthdate: ")
date = driver.find_element_by_name("dd")
date.send_keys(date_)

#Finds element with name "yyyy"
year_ = input("\nEnter your birth year:")
year = driver.find_element_by_name("yyyy")
year.send_keys(year_)

submit = driver.find_element_by_id("reg-submit-button")
submit.click()
