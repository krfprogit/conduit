from selenium import webdriver
import time
from csv import reader

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def xpath(browser, xpath_search):
    return browser.find_element_by_xpath(xpath_search)


def homepage(browser):
    time.sleep(2)
    print(f"conduit homepage:", {browser.current_url})


def accept_cookies(browser):
    browser.find_element_by_xpath('//button[contains (.,"I accept!")]').click()
    time.sleep(2)


def login(browser, user_login):
    xpath(browser, '//*[@href="#/login"]').click()
    time.sleep(1)
    for k, v in user_login.items():
        xpath(browser, f'//*[@placeholder="{k}"]').send_keys(v)
    time.sleep(1)
    xpath(browser, '//button[1]').click()
    time.sleep(1)


def add_new_article(browser, input_data):
    article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]
    browser.find_element_by_xpath('//*[@href="#/editor"]').click()
    time.sleep(2)

    article_filling = []
    i = 0
    while i < len(input_data):
        fill = browser.find_element_by_xpath(f'//*[@placeholder="{article_data[i]}"]').send_keys(input_data[i])
        article_filling.append(fill)
        i += 1

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
