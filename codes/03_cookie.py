from selenium import webdriver
import time

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")

browser.maximize_window()
time.sleep(2)

button_accept = browser.find_element_by_xpath('//button[contains (.,"I accept!")]')
button_accept.click()
time.sleep(2)

button_list = browser.find_elements_by_xpath('//button')
assert (button_list == [])

browser.quit()
