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