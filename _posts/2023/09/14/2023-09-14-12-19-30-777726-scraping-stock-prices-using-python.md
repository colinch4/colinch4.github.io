---
layout: post
title: "Scraping stock prices using Python"
description: " "
date: 2023-09-14
tags: [WebScraping]
comments: true
share: true
---

In this blog post, we will learn how to scrape stock prices using Python. Web scraping is a technique used to extract data from websites. By utilizing Python libraries such as BeautifulSoup and Requests, we can automate the process of fetching stock prices from popular financial websites.

## Installation

First, let's make sure we have the required libraries installed. Open your terminal and run the following command to install BeautifulSoup and Requests:

```
pip install beautifulsoup4 requests
```

## Fetching the HTML

We will start by fetching the HTML content of the webpage that contains the stock prices. In this example, we will use Yahoo Finance as our source. To do this, we need to send an HTTP GET request to the URL of the webpage and retrieve the HTML response.

```python
import requests

url = 'https://finance.yahoo.com/quote/AAPL'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    print(html)
```

## Parsing the HTML

Now that we have the HTML content, we need to parse it to extract the relevant information. BeautifulSoup provides a convenient way to navigate and search the HTML document. We can use CSS selectors or HTML tags to find elements containing the stock prices.

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

current_price = soup.select_one('.D(ib) .Trsdu(0.3s) .Fw(b) .Fz(36px)').text
change = soup.select_one('.D(ib) .Trsdu(0.3s) .Fw(500) .Fz(24px)').text

print(f"Current Price: {current_price}")
print(f"Change: {change}")
```

## Putting it Together

Let's put everything together and create a function that takes a stock symbol as input and returns the current price and change.

```python
def get_stock_price(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        current_price = soup.select_one('.D(ib) .Trsdu(0.3s) .Fw(b) .Fz(36px)').text
        change = soup.select_one('.D(ib) .Trsdu(0.3s) .Fw(500) .Fz(24px)').text
        return current_price, change

symbol = 'AAPL'
price, change = get_stock_price(symbol)
print(f"Current Price for {symbol}: {price}")
print(f"Change: {change}")
```

## Conclusion

In this blog post, we learned how to scrape stock prices using Python. By using libraries like BeautifulSoup and Requests, we can fetch the HTML content of a webpage and extract the relevant information. Web scraping can be a powerful tool for collecting and analyzing data from websites, but it's important to be aware of the terms of service of the websites you are scraping and to use scraping responsibly.

#Python #WebScraping