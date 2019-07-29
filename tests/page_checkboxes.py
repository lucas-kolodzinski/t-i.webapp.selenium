__author__ = "Lucas Kolodzinski"

from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages
import time

class PageCheckboxes(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.Checkboxes(self.driver)
        self.page_link = self.test_object.page_link()
        self.page_link.click()

    def test_1_page_header(self):
        expected_header = "Checkboxes"
        current_header = self.test_object.page_header()
        self.assertEqual(current_header, expected_header, "Current header does not meet expectations")

    def test_2_checkboxes(self):
        first_checkbox = self.test_object.first_checkbox()
        second_checkbox = self.test_object.second_checkbox()
        checkboxes = [first_checkbox, second_checkbox]
        for i in checkboxes:
            if i.get_attribute("checked") is False:
                i.click()
                time.sleep(2)
            else:
                i.click()
                time.sleep(2)