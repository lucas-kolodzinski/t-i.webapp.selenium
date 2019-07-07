__author__ = "Lucas Kolodzinski"

from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages
import time


class PageABTesting(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.PageABTesting(self.driver)
        self.link = self.test_object.page_link()
        self.link.click()
        time.sleep(2)

    def test_1_page_link(self):
        actual_page_url = self.driver.current_url
        expected_page_url = 'https://the-internet.herokuapp.com/abtest'
        self.assertEqual(actual_page_url, expected_page_url, "Page url does not meet expectation")

    def test_2_page_header(self):
        actual_header = self.test_object.page_header()
        expected_header = "A/B Test Variation 1"
        self.assertEqual(actual_header, expected_header, "Page title is different than expected")

    def test_3_paragraph_content(self):
        actual_paragraph_content = self.test_object.paragraph_content()
        print(actual_paragraph_content)
        expected_paragraph_content = ""
        with open("page_abtesting_content.txt", 'r') as file:
            expected_paragraph_content = file.read()
        #print(expected_paragraph_content)
        self.assertEqual(actual_paragraph_content, expected_paragraph_content, "Paragraph content does not follow expectations")