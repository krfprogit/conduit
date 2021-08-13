from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")
browser.maximize_window()
time.sleep(2)

# cookie
browser.find_element_by_xpath('//button[2]').click()

browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
email = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
email.send_keys("user69@gmail.hu")
password.send_keys("irsai10TC")
time.sleep(2)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(2)

user_name = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/user69'))
)

assert user_name.text == "user69"
print(f"login: {user_name.text}")
time.sleep(2)

# add_new_article
new_article = browser.find_element_by_xpath('//*[@href="#/editor"]')
new_article.click()
time.sleep(2)

input_data = ["cim", "ez", "a", "test"]
article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]
# print(f"{input_data[0]}, placeholder=\"{article_data[1]}\", {len(article_data)}")

article_filling = []
i = 0
while i < 4:
    fill = browser.find_element_by_xpath(f'//*[@placeholder="{article_data[i]}"]').send_keys(input_data[i])
    article_filling.append(fill)
    print(article_filling[i], i, input_data[i])
    i += 1

publish_button = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
time.sleep(2)

published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
assert (published_title.text == input_data[0])
print("New article published:", published_title.text)

browser.quit()
