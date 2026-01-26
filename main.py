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

# credentials are export to local terminal to be secure
username = os.environ.get("GITHUB_USERNAME")
password = os.environ.get("GITHUB_PASSWORD")

# send credentials to the Github
username_input = browser.find_element(By.ID, 'login_field').send_keys(username)
password_input = browser.find_element(By.ID, 'password').send_keys(password)

# after entering credentials find the sign in button and click
sign_in_button = browser.find_element(By.NAME, "commit")
sign_in_button.click()

# waiting for Github to respond
wait = WebDriverWait(browser, 15)

profile_button = wait.until(EC.presence_of_element_located(
    (By.XPATH, f"//*[@data-login='{username}']")))

print("Verified the GitHub login successfully!")

# no need for human confirmation anymore
browser.quit()
