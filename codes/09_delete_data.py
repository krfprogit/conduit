from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")

browser.maximize_window()
time.sleep(2)

browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()

browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
email = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
email.send_keys("a@a.hu")
password.send_keys("aaaAAA111")
time.sleep(2)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(2)

user_name = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a'))
    #    EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and text()="user2"]'))
)
assert user_name.text == "a"
print(f"login: {user_name.text}")
time.sleep(2)

# delete data
# user = browser.find_element_by_xpath('//*[@class="nav-link" and text()="a"]')
user_name.click()
time.sleep(2)

title_old = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@class="preview-link"]/h1'))
)
title_old.click()
time.sleep(4)

delete_article_button = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/span/button/span'))
).click()
time.sleep(2)

browser.refresh()
time.sleep(2)

# assert (browser.current_url == f'http://localhost:1667/#/articles/{browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')}')

print(browser.current_url)

browser.quit()
