from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import json

# credentials are export to local terminal to be secure
username = os.environ.get("GITHUB_USERNAME")
password = os.environ.get("GITHUB_PASSWORD")

options = Options()
options.add_argument("--start-maximized")  # optional: maximize window

browser = webdriver.Chrome(options=options)
browser.get("https://github.com")  # must load before adding cookies=

cookies_path = os.path.join(os.path.dirname(__file__), "cookies.json")

wait = WebDriverWait(browser, 15)

if os.path.exists(cookies_path):
    with open(cookies_path, "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        # Remove expiry if present to avoid errors
        cookie.pop('expiry', None)
        try:
            browser.add_cookie(cookie)
        except Exception:
            pass

    print("Cookies loaded from file")
    browser.refresh()  # Browser now behaves as logged in

else:
    # wait object for login

    # Click Sign in button
    sign_in_button = browser.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()

    # send credentials to the Github
    # wait.until to make sure everything was loaded
    username_input = wait.until(
        EC.presence_of_element_located((By.ID, 'login_field')))
    username_input.send_keys(username)

    password_input = wait.until(
        EC.presence_of_element_located((By.ID, 'password')))
    password_input.send_keys(password)
    password_input.submit()

    # Verifying login by comparing username with data login attribute
    profile_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//*[@data-login='{username}']")))

    print("Login successfully!")

    # Save cookies to a file
    cookies = browser.get_cookies()  # Get all cookies from the session

    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

    print("Cookies saved to file")

# no need for human confirmation anymore
browser.quit()
