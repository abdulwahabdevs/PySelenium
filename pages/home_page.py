from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def is_logged_in(self, username=None):
        button = self.browser.find_elements(
            By.CSS_SELECTOR, 'button[data-login]')
        if button:
            if username:
                return button[0].get_attribute("data-login") == username
            return True
        return False
