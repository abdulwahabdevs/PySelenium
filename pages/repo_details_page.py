from selenium.webdriver.common.by import By
from .base_page import BasePage


class RepoDetailsPage(BasePage):
    REPO_NAME = (By.CSS_SELECTOR, 'strong[itemprop="name"] a')

    def is_open(self, repo_name=None):
        if not self.is_element_visible(self.REPO_NAME):
            return False

        if repo_name:
            return self.get_text(self.REPO_NAME) == repo_name

        return True
