__author__ = "Lukasz Kolodzinski"

import unittest
import datetime
from selenium import webdriver

class TestFoundation(unittest.TestCase):
    """
        Basic class to initialize tests env
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        print("Tests execution started at:" str(datetime.datetime.now()))
        print("-----------------------------------")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
