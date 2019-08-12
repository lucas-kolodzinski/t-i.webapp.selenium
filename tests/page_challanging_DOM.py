__author__ = "Lucas Kolodzinski"

from selenium.webdriver.common.by import By
from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages

class ChallangingDOM(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.ChallangingDOM(self.driver)
        self.link = self.test_object.page_link()
        self.link.click()

    def test_1_page_header(self):
        actual_page_header = self.test_object.page_header()
        expected_page_header = "Challenging DOM"
        self.assertEqual(actual_page_header, expected_page_header, "Actual page header is not equal to expected header")

    def test_2_href_edit(self):
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[2]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[5]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[6]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[7]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[8]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[9]/td[7]/a[1]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[1]

        before_xpath = "/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr["
        after_xpath = "]/td[7]/a[1]"
        list_hrefs = []
        expected_amount_hrefs = 10
        for i in range(1, 11):
            actual_xpath = "/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[{}]/td[7]/a[1]".format(i)
            # actual_xpath = (before_xpath + str(i) + after_xpath)
            #print(actual_xpath)
            element = self.driver.find_element(By.XPATH, actual_xpath)
            list_hrefs.append(element)
            element.click()
            current_address = self.driver.current_url
            expected_address = "https://the-internet.herokuapp.com/challenging_dom#edit"
            if current_address == expected_address:
                self.driver.back()
            else:
                print("Test iteration number " + str(i) + "failed")
        #print(list_hrefs)
        #print(len(list_hrefs))
        self.assertEqual(len(list_hrefs), expected_amount_hrefs, "Table elements amount does not meet expectations")

    def test_3_delete_href(self):
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[2]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[5]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[6]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[7]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[8]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[9]/td[7]/a[2]
        # /html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[2]

        #before_xpath = "/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr["
        #after_xpath = "]/td[7]/a[2]"
        list_elements = []
        expected_amount_elements = 10
        for i in range(1,11):
            actual_xpath = "/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[{}]/td[7]/a[2]".format(i)
            #print(actual_xpath)
            element = self.driver.find_element(By.XPATH, actual_xpath)
            element.click()
            self.driver.back()

    def test_4_buttons(self):
        for i in range (1,4):
            buttons_xpath = "//*[@class='large-2 columns']/a[{}]".format(i)
            #print (buttons_xpath)
            button = self.driver.find_element(By.XPATH, buttons_xpath)
            if button.is_enabled() == True:
                button.click()
            else:
                print("Button {} is not enabled".format(i))

    def test_5_canvas(self):
        canvas = self.test_object.canvas()
        if canvas.is_displayed():
            print("Canvas is displayed")
        else:
            print("Canvas is not available")