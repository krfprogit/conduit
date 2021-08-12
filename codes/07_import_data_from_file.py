from selenium import webdriver
import time
from csv import reader

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")

browser.maximize_window()
time.sleep(2)

browser.find_element_by_xpath('//button[2]').click()

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

# import data from file
# input_data = ["ops", "1", "sor", "tag"]
# article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

input_file = 'input_articles.csv'

with open(input_file, 'r') as data:
    csv_reader = reader(data)
    # Get all rows of csv from csv_reader object as list of tuples
    input_data = list(map(tuple, csv_reader))
    # display all rows of csv
    # print(input_data)

print(input_data)
print(len(input_data))
print(input_data[0])
print(len(input_data[0]))
print(input_data[1])
# print(input_data[2])
# print(input_data[3])

# new article
new_article = browser.find_element_by_xpath('//*[@href="#/editor"]')
new_article.click()
time.sleep(2)

# fill_article = []
post_num = len(input_data) - 1
# +1 ?!?!?!
line_num = len(input_data[0])

for i in range(1, post_num):
    browser.find_element_by_xpath('//*[@href="#/editor"]').click()
    print(i, input_data[i][0], input_data[i][1], input_data[i][2], input_data[i][3])
    time.sleep(2)
    for j in range(0, line_num):
        browser.find_element_by_xpath(f'//*[@placeholder="{input_data[0][j]}"]').send_keys(input_data[i][j])
        # fill_article.append(fill)
    # print(i, input_data[i][0], input_data[i][1], input_data[i][2], input_data[i][3])
    time.sleep(2)
    #    publish_btn = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    publish_button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
    time.sleep(2)

#    print(i, input_data[i][j])

# assert
# published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
# assert(published_title.text == input_data[0])
# print("New article published:", published_title.text)

browser.quit()
