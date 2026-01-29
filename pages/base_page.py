from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, timeout=15):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def type(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
