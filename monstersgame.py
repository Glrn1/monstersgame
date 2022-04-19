from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.get('http://br4.monstersgame.moonid.net/') #login page
print('Title: %s' % browser.title)
time.sleep(2)
cookie = {"name": "GAMESESSID", "value": "cookie here"} #set coockie
browser.add_cookie(cookie)
cookie1 = {"name": "sessionid", "value": "cookie here", "domain" : ".moonid.net"} #set coockie
browser.add_cookie(cookie1)
cookie2 = {"name": "csrftoken", "value": "cookie here", "domain" : ".moonid.net"} #set coockie
browser.add_cookie(cookie2)
cookie3 = {"name": "_swa_uv", "value": "cookie here", "domain" : ".moonid.net"} #set coockie
browser.add_cookie(cookie3)
time.sleep(2)
browser.refresh()
time.sleep(2)
for i in range(5000):
	time.sleep(300)
	link = browser.find_element_by_link_text("Saque")
	link.click()
	time.sleep(1)
	continuar = browser.find_element_by_name("solevelmax")
	continuar.send_keys(Keys.ENTER)
	time.sleep(1)
	continua = browser.find_element_by_class_name("pageContentC").click()
	time.sleep(1)
	continua = browser.find_element_by_class_name("pageContentC").click()
	continua = browser.find_element_by_class_name("pageContentC").click()
	time.sleep(1)
	continua = browser.find_element_by_class_name("pageContentC").click()
	time.sleep(1)
	element = browser.find_element_by_css_selector("input[title='Ataque:']")
	browser.execute_script("arguments[0].click();", element)
	time.sleep(10)
	link = browser.find_element_by_link_text("Status").click()
browser.quit()
