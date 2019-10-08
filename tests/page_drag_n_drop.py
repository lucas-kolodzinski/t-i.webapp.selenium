from tests_base.base_class import EnvironmentSetup
from pages.fake_pages import FakePages
from selenium.webdriver import ActionChains

class DragAndDrop(EnvironmentSetup):

    def setUp(self):
        super().setUp()
        self.test_object = FakePages.DragAndDrop(self.driver)
        self.page_link = self.test_object.page_link()
        self.page_link.click()

    def test_1_page_header(self):
        expected_header = "Drag and Drop"
        actual_header = self.test_object.page_header()
        self.assertEqual(actual_header, expected_header, "Header don't match")

    def test_2_drag_object_a_and_drop(self):
        object_a = self.test_object.object_a()
        object_b = self.test_object.object_b()
        action = ActionChains(self.driver)
        action.drag_and_drop(object_a, object_b).perform()

    def test_3_drag_object_b_and_drop(self):
        object_a = self.test_object.object_a()
        object_b = self.test_object.object_b()
        action = ActionChains(self.driver)
        action.drag_and_drop(object_b, object_a).perform()