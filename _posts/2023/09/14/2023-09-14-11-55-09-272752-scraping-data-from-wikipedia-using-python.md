---
layout: post
title: "Scraping data from Wikipedia using Python"
description: " "
date: 2023-09-14
tags: [Python, WebScraping]
comments: true
share: true
---

In this tutorial, we will explore how to scrape data from Wikipedia using Python. Wikipedia is a valuable source of information, and being able to extract data from it can be useful for various purposes like research, analysis, or creating custom datasets.

## Preparing the Environment

Before we dive into the code, we need to make sure our environment is set up correctly. Here are the steps you need to follow:

1. Install the required libraries:
```python
pip install beautifulsoup4
pip install requests
```

2. Import the necessary modules:
```python
import requests
from bs4 import BeautifulSoup
```

## Scraping Wikipedia Page

To scrape data from Wikipedia, we first need to retrieve the HTML content of the desired page. We can achieve this using the `requests` library:

```python
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
page_content = response.content
```

Once we have the HTML content, we can use the `BeautifulSoup` library to parse and navigate the HTML structure:

```python
soup = BeautifulSoup(page_content, 'html.parser')
```

## Extracting Data

Now that we have the parsed HTML, we can start extracting the desired data. For example, let's extract the table of contents from the Wikipedia page:

```python
table_of_contents = soup.find(id='toc')
```

We can then loop through the table of contents to extract further information. For instance, to print the section titles, we can use:

```python
for item in table_of_contents.find_all('span', class_='toctext'):
    print(item.text)
```

You can adapt the code snippets above to extract other elements from the Wikipedia page, such as paragraphs, links, or images.

## Conclusion

Scraping data from Wikipedia using Python is a powerful technique to gather information from this vast online encyclopedia. We've shown you the basic steps to retrieve the HTML content and extract specific data using libraries like `requests` and `BeautifulSoup`. Remember to always be respectful to the website's policies and follow their terms of service when scraping data.

#Python #WebScraping