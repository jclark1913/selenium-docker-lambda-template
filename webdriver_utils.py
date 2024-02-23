from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import shutil

DEFAULT_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

PAGE_LOAD_TIMEOUT = 9
MAX_ATTEMPTS = 3


def setup_driver():
    """Returns a headless selenium webdriver instance.

    Returns:
        driver: Selenium driver instance
    """
    # Delete any tmp files from previous runs
    shutil.rmtree("/tmp", ignore_errors=True)

    # Arguments to run Chrome headless and without extras to avoid using memory.
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Argument to block images from loading.
    options.add_argument("--blink-settings=imagesEnabled=false")

    # NOTE: We may wish to cycle through a list of user agents in the future, instead.
    options.add_argument(f"user-agent={DEFAULT_HEADERS['user-agent']}")
    driver = webdriver.Chrome(options=options)

    # Set page load timeout
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    return driver


def reset_driver(driver):
    """Resets the webdriver by quitting and creating a new instance.

    Args:
        driver: Selenium driver instance
    """

    print("Resetting driver")
    logging.info("Resetting driver")
    driver.quit()
    return setup_driver()


def return_page_source_from_url(driver, url):
    """Uses webdriver to get soup from a URL."""

    attempts = 0
    result = None
    while attempts < 3:
        try:
            driver.get(url)
            result = driver.page_source
            break
        except Exception as e:
            print(f"Error getting page: {e}")
            logging.error(f"Error getting page: {e}")
            driver = reset_driver(driver)
            attempts += 1

    if attempts >= MAX_ATTEMPTS:
        print(f"Failed to get page after {attempts} attempts")
        logging.error(f"Failed to get page after {attempts} attempts")

    return result
