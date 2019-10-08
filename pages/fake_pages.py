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

    class Checkboxes(BaseClass):
        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.Checkboxes.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.Checkboxes.page_header).text

        def first_checkbox(self):
            return self.driver.find_element(By.CSS_SELECTOR, FakePagesLocators.Checkboxes.first_checkbox)

        def second_checkbox(self):
            return self.driver.find_element(By.CSS_SELECTOR, FakePagesLocators.Checkboxes.second_checkbox)

    class ChallangingDOM(BaseClass):
        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.ChallangingDOM.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.ChallangingDOM.page_header).text

        def canvas(self):
            return self.driver.find_element(By.ID, FakePagesLocators.ChallangingDOM.canvas)

    class ContextMenu(BaseClass):
        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.ContextMenu.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.ContextMenu.page_header).text

        def menu_area(self):
            return self.driver.find_element(By.ID, FakePagesLocators.ContextMenu.menu)

    class DragAndDrop(BaseClass):
        def page_link(self):
            return self.driver.find_element(By.LINK_TEXT, FakePagesLocators.DragAndDrop.page_link)

        def page_header(self):
            return self.driver.find_element(By.TAG_NAME, FakePagesLocators.DragAndDrop.page_header).text

        def object_a(self):
            return self.driver.find_element(By.ID, FakePagesLocators.DragAndDrop.object_a)

        def object_b(self):
            return self.driver.find_element(By.ID, FakePagesLocators.DragAndDrop.object_b)