from selenium import webdriver
browser = webdriver.Firefox(executable_path = 'geckodriver')
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
# Calling the submit() method on any element
# will have the same result as clicking the Submit button for the form that
# element is in. (You could have just as easily called emailElem.submit(), and
# the code would have done the same thing.)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
htmlElem.send_keys(Keys.HOME) # scrolls to top
#Calling browser .find_element_by_tag_name('html') is a good place to send keys to the general
# web page. This would be useful if, for example, new content is loaded once
# you’ve scrolled to the bottom of the page.