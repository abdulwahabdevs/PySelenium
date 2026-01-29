from selenium.webdriver.common.by import By
from .base_page import BasePage


class ReposPage(BasePage):
    REPO_LIST = (By.CSS_SELECTOR, 'ul[data-listview-component="item-list"]')
    REPO_COUNT = (By.CSS_SELECTOR, 'span[class*="ReposCountText"]')

    def is_open(self):
        return self.is_element_visible(self.REPO_LIST)

    def get_repo_names(self):
        pass

    def get_repo_count(self):
        pass
