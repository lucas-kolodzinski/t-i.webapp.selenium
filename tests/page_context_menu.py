from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages
from selenium.webdriver import ActionChains
import time

class ContextMenu(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.ContextMenu(self.driver)
        self.page_link = self.test_object.page_link()
        self.page_link.click()

    def test_1_page_header(self):
        expected_header = "Context Menu"
        current_header = self.test_object.page_header()
        self.assertEqual(expected_header, current_header, "Header does not match expected")

    def test_2_context_menu(self):
        menu_area = self.test_object.menu_area()
        action = ActionChains(self.driver)
        action.context_click(menu_area).perform()
        #time.sleep(3)
