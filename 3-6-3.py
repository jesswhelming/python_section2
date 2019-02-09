from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
# driver = webdriver.Chrome('/Users/jeesuyang/Documents/section3/webdriver/chrome/chromedriver')
# driver.get('https://www.google.com')
# time.sleep(5)
#
# driver.save_screenshot('/Users/jeesuyang/Documents/section3/Chrome.png')
#
# driver.quit()
#
# print('완료')


#headless로 만들기

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path='/Users/jeesuyang/Documents/section3/webdriver/firefox/geckodriver')

driver.get('https://google.com')

driver.save_screenshot('/Users/jeesuyang/Documents/section3/headless_firefox.png')
driver.quit()

print('완료')
