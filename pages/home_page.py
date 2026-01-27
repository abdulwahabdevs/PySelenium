from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    USER_MENU_BUTTON = (By.CSS_SELECTOR, "button[data-login]")
    USER_MENU_OVERLAY = (By.CSS_SELECTOR,
                         'div[data-component="AnchoredOverlay"][role="dialog"][data-visibility-visible]')

    REPOSITORIES_BUTTON = (By.CSS_SELECTOR, 'a[href$="/repos"]')

    NOTIFICATIONS_BUTTON = (By.CSS_SELECTOR, 'a[href="/notifications"]')

    def is_logged_in(self, username=None):
        if not self.is_element_visible(self.USER_MENU_BUTTON):
            return False

        if username:
            button = self.wait_for_element(self.USER_MENU_BUTTON)
            return button.get_attribute("data-login") == username

        return True

    def open_user_menu(self):
        self.click(self.USER_MENU_BUTTON)
        self.wait_for_element(self.USER_MENU_OVERLAY)

    def go_to_repositories(self):
        self.click(self.REPOSITORIES_BUTTON)
        self.wait.until(EC.url_contains("/repos"))

    def go_to_notifications(self):
        self.click(self.NOTIFICATIONS_BUTTON)
