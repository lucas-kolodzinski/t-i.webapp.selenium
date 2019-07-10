__author__ = 'Lucas Kolodzinski'

from locators.fake_pages_selectors import FakePagesLocators
from selenium.webdriver.common.by import By


class BaseClass:

    def __init__(self, driver):
        self.driver = driver


class FakePages:
    """Describing element of particular training fake pages"""

    class PageABTesting(BaseClass):

        def page_link(self):
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, FakePagesLocators.PageABtesting.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.PageABtesting.page_header).text

        def paragraph_content(self):
            return self.driver.find_element(By.CSS_SELECTOR, FakePagesLocators.PageABtesting.paragraph).text

    class PageAddRemoveElements(BaseClass):

        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.PageAdRemoveElements.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.PageAdRemoveElements.page_header).text

        def button(self):
            return self.driver.find_element(By.XPATH, FakePagesLocators.PageAdRemoveElements.button)

        def delete_button(self):
            return self.driver.find_element(By.CLASS_NAME, FakePagesLocators.PageAdRemoveElements.delete_button)
