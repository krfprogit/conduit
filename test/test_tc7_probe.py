from selenium import webdriver
import time
from csv import reader

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import *

############################################ variables

URL = 'http://localhost:1667'

user_input = {"Username": "a",
              "Email": "a@a.hu",
              "Password": "aaaAAA111"
              }

user_login = {"Email": "a@a.hu",
              "Password": "aaaAAA111"
              }

# Test_6_add new article
input_data = ["cim", "ez", "a", "test"]

# Test_7_import data from file
input_file = 'test/input_articles.csv'

# Test_8_modify data
input_data_modify = ["Old title", "en", "vmi", "tag1"]
title = "uj cim"

# Test_9_delete data
input_data_delete = ["torolni kellene", "letorolni", "ez el fog tunni", "del"]


def conduit_webdriverwait(browser, value):
    element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, value))
    )
    return element


########################################### testing

class TestConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get(URL)
        time.sleep(1)

    def teardown(self):
        self.browser.quit()

    ########################################## Test_7 import data from file

    def test_import_data_from_file(self):
        accept_cookies(self.browser)

        login(self.browser, user_login)

        with open(input_file, 'r') as data:
            csv_reader = reader(data)
            input_data = list(map(tuple, csv_reader))
        print(f"Test_7: {len(input_data)} new articles published from file: {input_file}", end=" ")
        for i in range(1, len(input_data) - 1):  # every line
            xpath(self.browser, '//*[@href="#/editor"]').click()
            time.sleep(2)
            for j in range(0, len(input_data[0])):  # fill the form
                time.sleep(3)
                xpath(self.browser, f'//*[@placeholder="{input_data[0][j]}"]').send_keys(input_data[i][j])
            time.sleep(2)

            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
            time.sleep(5)

            published_title = xpath(self.browser, '//*[@class="container"]/h1')
            assert (published_title.text == input_data[i][0])
            print(f"{published_title.text}", sep=", ", end="; ")
