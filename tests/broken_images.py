__author__ = "Lucas Kolodzinski"

import requests
from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages

class PageBrokenImages(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.BrokenImages(self.driver)
        self.link = self.test_object.page_link()
        self.link.click()

    def test_1_check_page_header(self):
        expected_page_header = "Broken Images"
        actual_page_header = self.test_object.page_header()
        self.assertEqual(expected_page_header, actual_page_header, "Page header does not meet expectations")

    def test_2_check_images(self):
        first_image = self.test_object.first_image()
        second_image = self.test_object.second_image()
        third_image = self.test_object.third_image()
        images_list = [first_image, second_image, third_image]
        #print(images_list)

        for image in images_list:
            if (requests.head(image.get_attribute("src")).status_code==200):
                print("Valid image")
            else:
                print("Broken image")