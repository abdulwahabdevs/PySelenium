from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.repos_page import ReposPage
from pages.repo_details_page import RepoDetailsPage

import os
import json


def load_cookies(browser, path):
    if not os.path.exists(path):
        return False

    with open(path, "r") as file:
        cookies = json.load(file)

    for cookie in cookies:
        cookie.pop('expiry', None)
        try:
            browser.add_cookie(cookie)
        except Exception:
            pass

    return True


def save_cookies(browser, path):
    cookies = browser.get_cookies()
    with open(path, "w") as file:
        json.dump(cookies, file)


def main():
    options = Options()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    cookies_path = "cookies.json"

    browser.get("https://github.com")

    load_cookies(browser, cookies_path)
    browser.refresh()

    home_page = HomePage(browser)

    if home_page.is_logged_in():
        print("Already logged in (cookies worked!)")
    else:
        print("Not logged in yet - performing UI login")
        username = os.getenv("GITHUB_USERNAME")
        password = os.getenv("GITHUB_PASSWORD")

        login_page = LoginPage(browser)
        login_page.open()
        login_page.login(username, password)

        if home_page.is_logged_in(username):
            save_cookies(browser, cookies_path)
            print("Loggin and cookies saved")
        else:
            print("Login failed")

    home_page.go_to_repositories()

    repos_page = ReposPage(browser)
    assert repos_page.is_open()
    repos_page.go_to_my_repos()
    assert repos_page.is_my_repos_page_open()
    print("Found", repos_page.get_repo_count())
    for index, repo in enumerate(repos_page.get_repo_names()):
        print(index + 1, repo)

    repos_page.open_repo_by_name("abdulwahabdevs/PySelenium")

    repo_page = RepoDetailsPage(browser)
    assert repo_page.is_open("PySelenium")
    print(browser.current_url)

    print("Repo page confirmed")

    input("Press 'Enter' to exit>>>")
    browser.quit()


if __name__ == "__main__":
    main()
