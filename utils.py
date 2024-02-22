from webdriver_utils import (
    setup_driver,
    reset_driver,
    return_page_source_from_url,
)


def get_page_source_from_generic_url(url):
    """Returns a soup object from a single URL. This can be used to get all HTML
    from the DOM of a webpage. This will NOT work for pages that require
    an active webdriver and dynamic JS.

    Args:
        url: URL to scrape

    Returns:
        soup: BeautifulSoup object
    """
    driver = setup_driver()
    soup = return_page_source_from_url(driver, url)
    driver.quit()
    return soup
