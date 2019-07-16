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