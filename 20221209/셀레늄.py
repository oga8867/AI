from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import selenium


# chrome_driver_path = "C:/Users/user/Downloads/chromedriver"
driver= webdriver.Chrome()
driver.implicitly_wait(3)  #로딩 기다리는 시간
# input()
# driver.get('https://www.google.com')

elem = driver.find_element(By.NAME, 'q')
elem.clear()
search = 'doctorwho'
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#이미지 메뉴 누르기
driver.find_element(By.XPATH, 'id="tsuid_61"')
# selenium_scroll_option(driver)
# img_srcs = driver.find_elements(By.CLASS_NAME,'rg_i')                       )