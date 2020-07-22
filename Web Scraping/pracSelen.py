from selenium import webdriver

browser = webdriver.Firefox(executable_path = 'geckodriver')
browser.get('http://inventwithpython.com')
try:
	elem = browser.find_element_by_partial_link_text("Automate the Boring")
	print('Found <%s> element with that class name!' % (elem.tag_name))
	elem.click()
except:
	print('Was not able to find an element with that name.')