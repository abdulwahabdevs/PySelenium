from selenium.webdriver.common.by import By
from .base_page import BasePage


class RepoDetailsPage(BasePage):
    REPO_NAME_HEADER = (By.CSS_SELECTOR, 'strong[itemprop="name"] a')
    REPO_DESCRIPTION = (By.CSS_SELECTOR, 'p.f4.my-3')
    README_CONTAINER = (By.CSS_SELECTOR, 'article.markdown-body')

    def is_open(self, repo_name=None):
        if not self.is_element_visible(self.REPO_NAME_HEADER):
            return False

        if repo_name:
            return self.get_text(self.REPO_NAME_HEADER) == repo_name

        return True

    def get_repo_name(self):
        return self.get_text(self.REPO_NAME_HEADER)

    def get_repo_description(self):
        try:
            return self.get_text(self.REPO_DESCRIPTION)
        except:
            return None

    def get_readme_content(self):
        try:
            return self.get_text(self.README_CONTAINER)
        except:
            return None
