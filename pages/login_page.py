from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign in")

    USERNAME_INPUT = (By.ID, "login_field")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")

    def open(self):
        self.browser.get("https://github.com")

        # Click Sign in only if visible
        if self.is_element_visible(self.SIGN_IN_LINK):
            self.click(self.SIGN_IN_LINK)

        if self.is_element_visible(self.USERNAME_INPUT):
            self.wait_for_element(self.USERNAME_INPUT)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SIGN_IN_BUTTON)
