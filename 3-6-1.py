import requests

from selenium import webdriver

driver = webdriver.PhantomJS('/Users/jeesuyang/Documents/section3/webdriver/phantomjs/phantomjs')
driver.implicitly_wait(5)

driver.get('https://www.google.com')
driver.save_screenshot('/Users/jeesuyang/Documents/section3/website1.png')

driver.implicitly_wait(5)
driver.get('https://www.daum.net')
driver.save_screenshot('/Users/jeesuyang/Documents/section3/website2.png')

driver.quit()

print('스크린샷 완료')
