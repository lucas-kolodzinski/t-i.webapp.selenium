__author__ = 'Lukasz Kolodzinski'

from locators.home_page_selectors import HomePageLocators


class HomePage():
    """
        describing page elements for http://the-internet.herokuapp.com/
    """

    def __init__(self, driver):
        self.driver = driver

    def page_header_h1(self):
        return self.driver.find_element_by_xpath(HomePageLocators.page_header).text

    def page_subheading(self):
        return self.driver.find_element_by_xpath(HomePageLocators.page_subheading)
