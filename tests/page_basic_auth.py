from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

class BaseAuthAlert(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.BasicAuth(self.driver)

    def test_1_log_with_correct_data(self):
        expected_page_header = "Basic Auth"
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(2)
        actual_page_header = self.test_object.correct_logged_in()
        self.assertEqual(expected_page_header, actual_page_header, "Login operation didn't pass correctly")

    def test_2_log_without_password(self):
        try:
            self.driver.get("https://admin:@the-internet.herokuapp.com/basic_auth")
            time.sleep(2)
            expected_content = "Not authorized"
            actual_content = self.test_object.incorrect_login()
            self.assertEqual(expected_content, actual_content, "Login didn't fail as expected")
        except UnexpectedAlertPresentException:
            print ("Login failed, as expected")