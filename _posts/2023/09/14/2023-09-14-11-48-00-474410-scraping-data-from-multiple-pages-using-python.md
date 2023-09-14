---
layout: post
title: "Scraping data from multiple pages using Python"
description: " "
date: 2023-09-14
tags: [Python, WebScraping]
comments: true
share: true
---

In this tutorial, we will learn how to scrape data from multiple pages using Python. Web scraping is an automated method used to extract data from websites. We will be using the BeautifulSoup library to parse HTML and retrieve the required data.

## Prerequisites

Before we begin, make sure you have the following packages installed:
- Python (version 3 or above)
- BeautifulSoup (`pip install beautifulsoup4`)

## Steps to Scrape Data from Multiple Pages

1. Import the required libraries:
```python
import requests
from bs4 import BeautifulSoup
```

2. Define the URL of the first page you want to scrape:
```python
url = "https://example.com/page1"
```

3. Send an HTTP GET request to the URL:
```python
response = requests.get(url)
```

4. Parse the HTML content of the response using BeautifulSoup:
```python
soup = BeautifulSoup(response.content, "html.parser")
```

5. Extract the data you need from the parsed HTML:
```python
data = soup.find("div", class_="container").text
```

6. Loop through the remaining pages and repeat the steps above:
```python
for i in range(2, 6):
    url = f"https://example.com/page{i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data += soup.find("div", class_="container").text
```

7. Print or store the scraped data as per your requirement:
```python
print(data)
```

## Summary

By following these steps, you can easily scrape data from multiple pages using Python and BeautifulSoup. Remember to respect the website's terms of service and avoid excessive requests to prevent your IP from getting blocked. Happy scraping!

#Python #WebScraping