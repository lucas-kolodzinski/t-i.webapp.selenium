__author__ = 'Lukasz Kolodzinski'
from selenium.webdriver.common.by import By
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
        return self.driver.find_element_by_tag_name(HomePageLocators.page_subheading).text

    def hyperlinks_list(self):
        return self.driver.find_elements_by_xpath(HomePageLocators.list_of_links)

    def page_footer(self):
        return self.driver.find_element(By.LINK_TEXT, "Elemental Selenium")

    def image_link(self):
        return self.driver.find_element(By.XPATH, HomePageLocators.image_link)
