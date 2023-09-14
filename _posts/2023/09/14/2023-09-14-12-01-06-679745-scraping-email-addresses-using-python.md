---
layout: post
title: "Scraping email addresses using Python"
description: " "
date: 2023-09-14
tags: [Python, WebScraping]
comments: true
share: true
---

In this tutorial, we will learn how to scrape email addresses from a web page using Python. Web scraping is the process of extracting data from websites, and Python provides various libraries such as BeautifulSoup and requests to perform this task effectively.

## Prerequisites

To follow this tutorial, you should have a basic understanding of the Python programming language and have Python installed on your machine. Additionally, you will need to install the `beautifulsoup4` and `requests` libraries. You can install these libraries using pip:

```python
pip install beautifulsoup4
pip install requests
```

## Steps to Scrape Email Addresses

1. Import the necessary libraries:

   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. Make a GET request to the web page you want to scrape:

   ```python
   url = "https://example.com"
   response = requests.get(url)
   ```

3. Create a BeautifulSoup object to parse the HTML content:

   ```python
   soup = BeautifulSoup(response.content, 'html.parser')
   ```

4. Find all the email addresses on the web page:

   ```python
   email_addresses = []
   for link in soup.find_all('a'):
       href = link.get('href')
       if href and href.startswith("mailto:"):
           email_addresses.append(href[7:])
   ```

   The above code loops through all the `<a>` (anchor) tags on the web page and checks if the href attribute starts with "mailto:". If it does, the email address is extracted and added to the `email_addresses` list.

5. Print or use the scraped email addresses:

   ```python
   for email in email_addresses:
       print(email)
   ```

   You can modify this code to save the email addresses to a file, store them in a database, or perform any other desired action.

## Conclusion

Web scraping using Python provides a powerful way to extract data from websites. In this tutorial, we learned how to scrape email addresses from a web page using the `beautifulsoup4` and `requests` libraries. Remember to respect the website's terms of service and be responsible while scraping data from websites.

#Python #WebScraping