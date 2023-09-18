---
layout: post
title: "Scraping data from Google search results using Python"
description: " "
date: 2023-09-14
tags: [webscraping]
comments: true
share: true
---

In this tutorial, we will explore how to scrape data from Google search results using Python. Web scraping is a technique used to extract data from websites, and Google search results page is a common target for scraping.

## Prerequisites
To follow this tutorial, you should have the following installed:
- Python (version 3 or higher)
- Beautiful Soup library (for HTML parsing)
- Requests library (for making HTTP requests)

## Steps to Scrape Google Search Results

### Step 1: Install the required libraries
Open your terminal or command prompt and execute the following commands to install the necessary libraries:

```
pip install beautifulsoup4
pip install requests
```

### Step 2: Import the required libraries
Create a new Python file and import the `BeautifulSoup` and `requests` libraries.

```python
from bs4 import BeautifulSoup
import requests
```

### Step 3: Send a GET request to Google search
Now, let's define a function that takes a search query as input and returns the HTML content of the Google search results page.

```python
def get_google_results(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    return response.content
```

### Step 4: Parse the HTML and extract data
Let's define another function that takes the HTML content of the search results page and extracts the desired data. In this example, we will extract the titles and URLs of the search results.

```python
def parse_google_results(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("div", class_="g")
    
    for result in results:
        title = result.find("h3").get_text()
        url = result.find("a")["href"]
        
        print(f"Title: {title}")
        print(f"URL: {url}\n")
```

### Step 5: Run the code
Finally, let's call the functions to test our code. Pass the search query as an argument to the `get_google_results()` function and then pass the HTML content to the `parse_google_results()` function.

```python
# Example usage
query = "web scraping"
html = get_google_results(query)
parse_google_results(html)
```

## Conclusion
Web scraping can be a powerful tool for extracting data from websites, and in this tutorial, we learned how to scrape data from Google search results using Python. Remember to respect the website's terms of service and use web scraping responsibly.

#python #webscraping