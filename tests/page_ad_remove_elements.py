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

    def test_1_verify_page_url(self):
        actual_page_url = self.driver.current_url
        expected_page_url = "https://the-internet.herokuapp.com/add_remove_elements/"
        self.assertEqual(actual_page_url, expected_page_url, "Url does not meet expectations")

    def test_2_verify_page_header(self):
        expected_page_header ="Add/Remove Elements"
        actual_page_header = self.test_object.page_header()
        self.assertEqual(actual_page_header, expected_page_header, "Title values does not match")

    def test_3_check_if_add_button_is_enabled(self):
        add_button = self.test_object.button()
        if add_button.is_enabled() == True:
            add_button.click()
        else:
            print("Cannot click Add Button")

    def test_4_click_button_many_times(self):
        add_button = self.test_object.button()
        for i in range (0, 5):
            if add_button.is_enabled() == True:
                add_button.click()
            else:
                print("Cannot click Add button")

    def test_5_check_if_delete_button_is_enabled(self):
        add_button = self.test_object.button()
        if add_button.is_enabled() == True:
            add_button.click()
            time.sleep(2)
        else:
            print("Cannot click add button")

        delete_button = self.test_object.delete_button()
        if delete_button.is_enabled() == True:
            delete_button.click()
        else:
            print("Cannot click delete button")


