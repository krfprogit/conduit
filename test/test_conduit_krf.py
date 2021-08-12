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

    ########################################## Test_0_homepage

    def test_homepage(self):
        time.sleep(2)
        assert self.browser.find_element_by_xpath('//div[@class="container"]/h1').text == "conduit"
        assert self.browser.find_element_by_xpath(
            '//div[@class="container"]/p').text == "A place to share your knowledge."
        print(f"conduit homepage:, {self.browser.current_url}")

    ########################################## Test_3_cookies

    def test_cookies(self):
        xpath(self.browser, '//button[contains (.,"I accept!")]').click()
        time.sleep(2)
        assert (self.browser.find_elements_by_xpath('//button') == [])
        time.sleep(2)
