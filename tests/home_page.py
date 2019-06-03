__author__ = 'Lukasz Kolodzinski'

from pages.home_page import HomePage
from tests_base.base_class import EnvironmentSetup


class HomePageElements(EnvironmentSetup):

    def test_verify_home_page_header(self):
        test_object = HomePage(self.driver)
        self.assertEqual('Welcome to the-internet', test_object.page_header_h1(), 'Searched page header not found')
