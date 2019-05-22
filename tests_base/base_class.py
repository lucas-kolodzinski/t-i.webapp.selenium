import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.time = str(datetime.datetime.now())
        print("Test started at: {}".format(self.time))
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    #temporary test to verify base class work
    def test_abc(self):
        print("Page title is: {}".format(self.driver.title))

    def tearDown(self):
        print("Execution finished at: {}".format(self.time))
        self.driver.close()
        self.driver.quit()