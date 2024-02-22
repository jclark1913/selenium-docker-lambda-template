import json
from utils import get_page_source_from_generic_url, setup_driver


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def get_page_source(event, context):
    try:
        body = json.loads(event["body"])
        url = body["url"]
    except Exception as e:
        return {"statusCode": 400, "body": "Invalid request body"}

    driver = setup_driver()

    try:
        page_source = get_page_source_from_generic_url(driver, url)
    except Exception as e:
        driver.quit()
        return {"statusCode": 500, "body": f"Error getting {url}: {e}"}

    driver.quit()
    return {"statusCode": 200, "body": page_source}
