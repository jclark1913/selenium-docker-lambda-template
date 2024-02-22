from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import json


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/opt/chromedriver")

    body = json.loads(event["body"])
    url = body['url']

    options.binary_location = '/opt/chrome/chrome'
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    chrome = webdriver.Chrome(options=options, service=service)
    chrome.get(url)

    return chrome.page_source

# def get_page_source(event, context):
#     try:
#         body = json.loads(event["body"])
#         url = body["url"]
#     except Exception as e:
#         return {"statusCode": 400, "body": "Invalid request body"}

#     driver = setup_driver()

#     try:
#         page_source = get_page_source_from_generic_url(driver, url)
#     except Exception as e:
#         driver.quit()
#         return {"statusCode": 500, "body": f"Error getting {url}: {e}"}

#     driver.quit()
#     return {"statusCode": 200, "body": page_source}
