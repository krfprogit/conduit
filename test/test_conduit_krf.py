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

    ########################################## Test_5_scrolling

    def test_scrolling(self):
        accept_cookies(self.browser)

        login(self.browser, user_login)

        print(f"Test_5_scrolling:", end=" ")
        page_lists = self.browser.find_elements_by_class_name("page-link")
        for page in page_lists:
            page.click()
            print(page.text, sep=", ", end=" ")
            last_page = xpath(self.browser, f'//*[@class="page-item active" and @data-test="page-link-{page.text}"]')
            assert (page.text == last_page.text)
            print(f"last page: #{last_page.text}")

    ########################################## Test_6_add new article

    def test_add_new_data(self):
        article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

        accept_cookies(self.browser)
        login(self.browser, user_login)

        xpath(self.browser, '//*[@href="#/editor"]').click()
        time.sleep(2)

        article_filling = []
        i = 0
        while i < len(input_data):
            fill = xpath(self.browser, f'//*[@placeholder="{article_data[i]}"]').send_keys(input_data[i])
            article_filling.append(fill)
            i += 1
            time.sleep(1)
        time.sleep(2)

        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
        time.sleep(2)

        published_title = xpath(self.browser, '//*[@class="container"]/h1')
        publish_date = self.browser.find_element_by_class_name("date")
        assert (self.browser.current_url == f'http://localhost:1667/#/articles/{input_data[0]}')
        print(
            f"Test_6_new_article published with title: \"{published_title.text}\" on {publish_date.text} at {self.browser.current_url}")

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
                xpath(self.browser, f'//*[@placeholder="{input_data[0][j]}"]').send_keys(input_data[i][j])
            time.sleep(2)

            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
            time.sleep(5)

            published_title = xpath(self.browser, '//*[@class="container"]/h1')
            assert (published_title.text == input_data[i][0])
            print(f"{published_title.text}", sep=", ", end="; ")

    ########################################## Test_8 modify data

    def test_modify_data(self):
        accept_cookies(self.browser)

        login(self.browser, user_login)

        add_new_article(self.browser, input_data_modify)
        title_list = []
        title_list.append(title)

        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@a/"]'))
        ).click()
        time.sleep(2)

        old_title = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="preview-link"]/h1'))
        )
        title_list.append(old_title.text)
        old_title.click()
        time.sleep(2)

        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="article-meta"]/span/a/span'))
        ).click()
        time.sleep(2)

        new_title = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@placeholder="Article Title"]'))
        )
        new_title.clear()
        new_title.send_keys(title)
        time.sleep(2)

        xpath(self.browser, '//button[@type="submit"]').click()
        time.sleep(5)

        new_post_title = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="container"]/h1'))
        )
        title_list.append(new_post_title.text)
        time.sleep(2)

        # assert(self.browser.current_url == f'http://localhost:1667/#/articles/{title_list[2]}')
        assert (title_list[2] == title_list[0])
        print(f"Test_8_modify_data: article title changed: {title_list[1]} -> {title_list[2]}")

    ########################################## Test_9 delete data

    def test_delete_data(self):
        accept_cookies(self.browser)

        login(self.browser, user_login)

        add_new_article(self.browser, input_data_delete)
        time.sleep(2)

        url_deleted = self.browser.current_url
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="article-meta"]/span/button/span'))
        ).click()
        time.sleep(5)

        self.browser.refresh()

        assert (self.browser.current_url == 'http://localhost:1667/#/')
        print(f"Test_9_delete data: deleted url: {url_deleted}")
