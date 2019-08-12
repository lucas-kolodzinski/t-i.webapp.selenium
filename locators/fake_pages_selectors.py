__author__ = 'Lucas Kolodzinski'


class FakePagesLocators:
    """Selectors for elements of the rest of training content"""

    class PageABtesting:
        """Selectors for: http://the-internet.herokuapp.com/abtest"""

        # partial link text
        page_link = "A/B"

        # tag name
        page_header = "h3"

        # css selector
        paragraph = ".example > p:nth-child(2)"

    class PageAdRemoveElements:
        """https://the-internet.herokuapp.com/add_remove_elements/"""

        # link text
        page_link = "Add/Remove Elements"

        #css selector
        page_header = "#content > h3:nth-child(1)"

        #xpath
        button = "/html/body/div[2]/div/div/button"

        #class name
        delete_button = "added-manually"

    class BasicAuth:
        """ alert box with user authentication"""

        # tag name
        page_header = "h3"

        #tag name
        text_info = "body"

    class BrokenImages:
        """https://the-internet.herokuapp.com/broken_images"""

        #link text
        page_link = "Broken Images"

        #tag name
        page_header = "h3"

        #xpath
        first_image = "/html/body/div[2]/div/div/img[1]"
        second_image = "/html/body/div[2]/div/div/img[2]"
        third_image = "/html/body/div[2]/div/div/img[3]"

    class Checkboxes:
        """https://the-internet.herokuapp.com/checkboxes"""

        #link text
        page_link = "Checkboxes"

        #tag name
        page_header = "h3"

        #css_selector
        first_checkbox = "#checkboxes > input:nth-child(1)"
        second_checkbox = "#checkboxes > input:nth-child(3)"

    class ChallangingDOM:
        """https://the-internet.herokuapp.com/challenging_dom"""

        #link text
        page_link = "Challenging DOM"

        #tag_name
        page_header = "h3"

        #id
        canvas = "canvas"
