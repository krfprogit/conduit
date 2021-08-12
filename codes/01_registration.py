from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")
browser.get("http://localhost:1667")
browser.maximize_window()
time.sleep(2)

assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."

##################################################accept cookies

browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
time.sleep(2)

###################################################registration

user_input = {"name": "a",
              "email": "a@a.hu",
              "password": "aaaAAA111"
              }

browser.find_element_by_xpath('//*[@href="#/register"]').click()
username = browser.find_element_by_xpath('//*[@placeholder="Username"]')
email = browser.find_element_by_xpath('//*[@placeholder="Email"]')
password = browser.find_element_by_xpath('//*[@placeholder="Password"]')

username.send_keys(user_input["name"])
email.send_keys(user_input["email"])
password.send_keys(user_input["password"])
time.sleep(2)

browser.find_element_by_xpath('//button[1]').click()
time.sleep(2)

text_ref_success = "Welcome!"
text_ref_fail = "Registration failed!"

welcome = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
)

if welcome.text == text_ref_success:
    print(welcome.text)
    print(browser.find_element_by_css_selector(".swal-text").text)
elif welcome.text == text_ref_fail:
    print(welcome.text)
    print(browser.find_element_by_css_selector(".swal-text").text)
assert (welcome.text == text_ref_fail)

browser.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
time.sleep(2)

browser.quit()
