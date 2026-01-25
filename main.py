from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

options = Options()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=options)
browser.get("https://github.com")

sign_in_button = browser.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

username = os.environ.get("GITHUB_USERNAME")
password = os.environ.get("GITHUB_PASSWORD")

username_input = browser.find_element(By.ID, 'login_field').send_keys(username)
password_input = browser.find_element(By.ID, 'password').send_keys(password)


input("Press Enter to close...")
