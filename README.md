# docker-selenium-lambda-template

A basic configuration for setting up a Lambda function that uses Selenium and a stable Chrome webdriver (as of Feb 22, 2024) to scrape the source of a single webpage. Includes Dockerfile and serverless.yml w/ necessary dependencies.

To test deploy w/ serverless:
```bash
serverless deploy
```

Make a request to the endpoint:
```bash
curl -X POST {aws-lambda-url}/get_page_source -d '{"url": "https://www.example.com"}'
```

The request should return 200 and the page source of the requested URL as a JSON response.

Orginally a fork of the excellent and automatically updated [docker-selenium-lambda](https://github.com/umihico/docker-selenium-lambda) by [umihico](https://github.com/umihico). Stripped down and slightly modified for a specific use case for a project.
