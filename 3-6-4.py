from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome('/Users/jeesuyang/Documents/section3/webdriver/chrome/chromedriver')
driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
time.sleep(5)
driver.implicitly_wait(5)


driver.find_element_by_name('log').send_keys('jeesu29@gmail.com')
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('tndufdid878')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()


print('완료')
