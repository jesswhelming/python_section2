from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/jeesuyang/Documents/section3/webdriver/chrome/chromedriver')

driver.get('https://google.com')

driver.save_screenshot('/Users/jeesuyang/Documents/section3/headless_chrome.png')
driver.quit()

print('완료')
