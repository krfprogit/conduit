import time
from csv import reader

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import *

# # # # # # # # # # # # # # # # # # # # # # # # Defining variables # # # # # # # # # # # # # # # # # # # # # # # #

URL = 'http://localhost:1667'

user_input = {"Username": "user2",
              "Email": "user2@hotmail.com",
              "Password": "Userpass1"
              }

user_login = {"Email": "user2@hotmail.com",
              "Password": "Userpass1"
              }

# Test_6 new post
input_post = ["new", "me", "blabablabal", "key"]
# Test_7 import data from file
input_file = 'test/input_article.csv'
# Test_8 modify data
input_post_modify = ["Old title", "én", "lorem ipsum újra meg újra", "kulcs"]
title = "Módositom a cimet"
# Test_9 delete data
input_post_delete = ["Might be deleted", "én", "lorem ipsum újra meg újra", "kulcs"]


# # # # # # # # # # # # # # # # # # # # # # # # Testing Conduit App # # # # # # # # # # # # # # # # # # # # # # # #

class TestConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get(URL)
        time.sleep(1)

    def teardown(self):
        self.browser.quit()

    # # # # # # # # # # # # # # # # # # # # # # # # Test_7 IMPORT DATA FROM FILE # # # # # # # # # # # # # # # # # #

    def test__import_data_from_file(self):
        accept_cookies(self.browser)
        login(self.browser, user_login)
        with open(input_file, 'r') as data:
            csv_reader = reader(data)
            input_post = list(map(tuple, csv_reader))
        print(f"Test_7: {len(input_post)} new articles published from file: {input_file}", end=" ")
        for i in range(1, len(input_post) - 1):  # every line
            xpath(self.browser, '//*[@href="#/editor"]').click()
            time.sleep(2)
            for j in range(0, len(input_post[0])):  # fill the form
                xpath(self.browser, f'//*[@placeholder="{input_post[0][j]}"]').send_keys(input_post[i][j])
            time.sleep(2)
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
            time.sleep(5)
            # assert
            published_title = xpath(self.browser, '//*[@class="container"]/h1')
            assert (published_title.text == input_post[i][0])
            print(f"{published_title.text}", sep=", ", end="; ")
