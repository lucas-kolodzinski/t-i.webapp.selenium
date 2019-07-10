__author__ = "Lucas Kolodzinski"

import time
from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages

class PageAddRemoveElements(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.PageAddRemoveElements(self.driver)
        self.link = self.test_object.page_link()
        self.link.click()
        time.sleep(3)

    # def test_1_verify_page_url(self):
    #     actual_page_url = self.driver.current_url
    #     expected_page_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    #     self.assertEqual(actual_page_url, expected_page_url, "Url does not meet expectations")

    def test_2_verify_page_title(self):
        expected_page_title = self.test_object.page_header()
        actual_page_title = self.driver.title
        self.assertEqual(actual_page_title, expected_page_title, "Title values does not match")

