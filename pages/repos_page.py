from selenium.webdriver.common.by import By
from .base_page import BasePage


class ReposPage(BasePage):
    CONTRIBUTIONS_BUTTON = (By.CSS_SELECTOR, 'a[href="?q=contributed-by:@me"]')
    REPOS_BUTTON = (By.CSS_SELECTOR, 'a[href="?q=owner:@me"]')
    REPO_LIST = (By.CSS_SELECTOR, 'ul[data-listview-component="item-list"]')
    REPO_COUNT = (By.CSS_SELECTOR, 'span[class*="ReposCountText"]')

    def is_open(self):
        return self.is_element_visible(self.CONTRIBUTIONS_BUTTON)

    def go_to_my_repos(self):
        self.click(self.REPOS_BUTTON)

    def get_repo_names(self):
        pass

    def get_repo_count(self):
        pass
        # return self.get_text(self.REPO_COUNT)
