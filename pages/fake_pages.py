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

    class BasicAuth(BaseClass):
        def correct_logged_in(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.BasicAuth.page_header).text

        def incorrect_login(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.BasicAuth.text_info).text

    class BrokenImages(BaseClass):
        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.BrokenImages.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.BrokenImages.page_header).text

        def first_image(self):
            return self.driver.find_element(By.XPATH, FakePagesLocators.BrokenImages.first_image)

        def second_image(self):
            return self.driver.find_element(By.XPATH, FakePagesLocators.BrokenImages.second_image)

        def third_image(self):
            return self.driver.find_element(By.XPATH, FakePagesLocators.BrokenImages.third_image)