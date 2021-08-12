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


def conduit_login(browser, user_login):
    xpath(browser, '//*[@href="#/login"]').click()
    time.sleep(1)
    for k, v in user_login.items():
        xpath(browser, f'//*[@placeholder="{k}"]').send_keys(v)
    time.sleep(1)
    xpath(browser, '//button[1]').click()
    time.sleep(1)
