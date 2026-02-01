from selenium.webdriver.common.by import By
from .base_page import BasePage


class ReposPage(BasePage):
    CONTRIBUTIONS_BUTTON = (By.CSS_SELECTOR, 'a[href="?q=contributed-by:@me"]')
    MY_REPOS_HEADER = (
        By.CSS_SELECTOR, 'h1[data-testid="finder-header-title"] div[title="My repositories"]')
    REPO_LIST = (By.CSS_SELECTOR, 'ul[data-listview-component="items-list"]')
    REPO_COUNT = (
        By.CSS_SELECTOR, 'div[class*="ReposListContainer"] span[class*="ReposCountText"]')
    REPO_LINKS = (
        By.CSS_SELECTOR, 'a[data-component="listview-title-link"]')

    def is_open(self):
        return self.is_element_visible(self.CONTRIBUTIONS_BUTTON)

    def go_to_my_repos(self):
        self.browser.get("https://github.com/repos?q=owner:@me")
        self.wait_for_element(self.MY_REPOS_HEADER)
        print("Current url:", self.browser.current_url)

    def is_my_repos_page_open(self):
        return self.is_element_visible(self.MY_REPOS_HEADER)

    def get_repo_count(self):
        return self.get_text(self.REPO_COUNT)

    def get_repo_names(self):
        repo_list = self.wait_for_element(self.REPO_LIST)
        repo_elements = repo_list.find_elements(*self.REPO_LINKS)

        return [repo.text.strip() for repo in repo_elements if repo.text.strip()]

    def open_repo_by_name(self, repo_name):
        repo_list = self.wait_for_element(self.REPO_LIST)
        repo_elements = repo_list.find_elements(*self.REPO_LINKS)

        for repo in repo_elements:
            if repo.text.strip() == repo_name:
                repo.click()
                return

        raise Exception(f"Repository '{repo_name}' not found!")
