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

    def test_1_href_edit(self):
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