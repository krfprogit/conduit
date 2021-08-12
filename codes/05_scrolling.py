from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")

browser.maximize_window()
time.sleep(2)

# cookies
browser.find_element_by_xpath('//button[2]').click()
time.sleep(2)

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
)

assert user_name.text == "a"
print(f"login: {user_name.text}")
time.sleep(2)

page_lists = browser.find_elements_by_class_name("page-link")
for p in page_lists:
    p.click()
    print(p.text)
time.sleep(2)

last_page = browser.find_element_by_xpath(f'//*[@class="page-item active" and @data-test="page-link-{p.text}"]')
print("last page text:", last_page.text)

assert (p.text == last_page.text)

browser.quit()
