__author__ = 'Lukasz Kolodzinski'

import time
from pages.home_page import HomePage
from tests_base.base_class import EnvironmentSetup
from selenium.webdriver.common.by import By


class HomePageElements(EnvironmentSetup):

    def test_1_verify_page_url(self):
        actual_page_url = self.driver.current_url
        expected_page_url = 'https://the-internet.herokuapp.com/'
        self.assertEqual(actual_page_url, expected_page_url, 'Wrong page url')

    def test_2_verify_page_title(self):
        actual_page_title = self.driver.title
        expected_page_url = "The Internet"
        self.assertEqual(actual_page_title, expected_page_url, 'Wrong page title')

    def test_3_verify_home_page_header(self):
       test_object = HomePage(self.driver)
       self.assertEqual('Welcome to the-internet', test_object.page_header_h1(), 'Searched page header not found')

    def test_4_verify_home_page_subheading(self):
        test_object = HomePage(self.driver)
        self.assertEqual('Available Examples', test_object.page_subheading(), 'There is no searched subheader')

    def test_5_verify_hyperlinks_txt_values(self):
        expected_elements = []
        with open('hyperlinks_list.txt', 'r') as file:
            expected_elements = file.read().splitlines()
        # print(expected_elements)
        elem = HomePage(self.driver)
        actual_elements = []
        for i in elem.hyperlinks_list():
            actual_elements.append(i.text)
            #print(i.text)
        self.assertListEqual(expected_elements, actual_elements, "Hyperlinks txt does not meet expectations")

    def test_6_verify_hyperreferences(self):
        expected_amount_of_hrefs = []
        with open('hyperlinks_list.txt', 'r') as file:
            expected_amount_of_hrefs = file.read().splitlines()
        elems = HomePage(self.driver)
        actual_amount_of_hrefs = []
        for i in elems.hyperlinks_list():
            hrfs = i.find_elements(By.TAG_NAME, 'a')
            for x in hrfs:
                actual_amount_of_hrefs.append(i.get_attribute("href"))
        self.assertEqual(len(expected_amount_of_hrefs), len(actual_amount_of_hrefs))

    def test_7_verify_page_footer(self):
        test_object = HomePage(self.driver)
        test_object.page_footer().click()
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[1])
        actual_new_page_title = self.driver.title
        expected_new_page_title = "Elemental Selenium: Receive a Free, Weekly Tip on Using Selenium like a Pro"
        self.assertEqual(actual_new_page_title, expected_new_page_title, "New page title does not meet expectations")

    def test_8_verify_image_link(self):
        test_object = HomePage(self.driver)
        test_object.image_link().click()
        time.sleep(3)
        expected_new_page_title = "GitHub - tourdedave/the-internet: An example application that captures" \
                                  " prominent and ugly functionality found on the web. Perfect for writing" \
                                  " automated acceptance tests against."
        actual_new_page_title = self.driver.title
        self.assertEqual(actual_new_page_title, expected_new_page_title)