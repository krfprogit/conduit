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

    ########################################## Test_3_cookies

    def test_cookies(self):
        xpath(self.browser, '//button[contains (.,"I accept!")]').click()
        time.sleep(2)
        assert (self.browser.find_elements_by_xpath('//button') == [])
        time.sleep(2)

    ########################################## Test_1_registration

    def test_registration(self):
        accept_cookies(self.browser)

        xpath(self.browser, '//*[@href="#/register"]').click()
        time.sleep(2)

        for k, v in user_input.items():
            xpath(self.browser, f'//*[@placeholder="{k}"]').send_keys(v)
        time.sleep(2)

        xpath(self.browser, '//button[1]').click()
        time.sleep(2)

        text_ref_success = "Welcome!"
        text_ref_fail = "Registration failed!"
        welcome = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
        )

        assert (welcome.text == text_ref_success)
        print("Test_1_OK: ", welcome.text, end=" ")
        if welcome.text == text_ref_success:
            print(self.browser.find_element_by_css_selector(".swal-text").text, sep=" ")
        elif welcome.text == text_ref_fail:
            print(self.browser.find_element_by_css_selector(".swal-text").text, sep=" ")

        for k, v in user_input.items():
            print(k, v, sep=": ", end=";")

        xpath(self.browser, '//*[@class="swal-button swal-button--confirm"]').click()

    ########################################## Test_2_login

    def test_login(self):
        accept_cookies(self.browser)

        xpath(self.browser, '//*[@href="#/login"]').click()
        time.sleep(2)

        for k, v in user_login.items():
            xpath(self.browser, f'//*[@placeholder="{k}"]').send_keys(v)
        time.sleep(2)

        xpath(self.browser, '//button[1]').click()
        time.sleep(2)

        user_name = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"a")]'))
        )
        assert user_name.text == "a"
        print(f"Test_2_login: as {user_name.text}")

    ########################################## Test_4_data list

    def test_data_list(self):
        accept_cookies(self.browser)

        login(self.browser, user_login)

        active_links = self.browser.find_elements_by_xpath('//*[@href="#/"]')

        assert (xpath(self.browser, '//*[@href="#/"]') == active_links[0])
        print("Test_4_data list: active links on conduit homepage", self.browser.current_url)
        for k in active_links:
            print(k.text)
