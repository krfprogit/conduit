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
    browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@a/"]'))
                      # EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and text()="a"]'))
                      )
assert user_name.text == "a"
print(f"login: {user_name.text}")
time.sleep(2)

elements = browser.find_elements_by_class_name("article-preview")
titles = browser.find_elements_by_xpath('//*[@class="article-preview"]/a/h1')

print(browser.find_element_by_xpath('//*[@class="nav-link router-link-exact-active active"]').text)
for t in titles:
    print(t.text)
time.sleep(2)

print("len:", len(titles))
print(titles[0].text)
time.sleep(2)

assert (browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text == titles[0].text)

active_links = browser.find_elements_by_xpath('//*[@href="#/"]')

print("Test_4_data list: active links on conduit homepage ", browser.current_url)
time.sleep(2)

for l in active_links:
    print(l.text)
time.sleep(2)

assert (browser.find_element_by_xpath('//*[@href="#/"]') == active_links[0])

browser.quit()
