---
layout: post
title: "Scraping dynamic web pages using Python Goose"
description: " "
date: 2023-09-23
tags: [webscraping]
comments: true
share: true
---

In the world of web scraping, there are static web pages and dynamic web pages. While scraping static web pages is relatively straightforward, dealing with dynamic web pages can be more challenging. In this article, we will explore how to scrape dynamic web pages using Python Goose.

## What is Python Goose?

Python Goose is a Python library that allows you to extract content, such as articles and structured data, from web pages. It is especially useful when dealing with dynamic web pages where the content is loaded dynamically using JavaScript.

## Installing Python Goose

To get started, you need to install Python Goose. You can do so by running the following command in your terminal:

```bash
pip install python-goose
```

## Scraping Dynamic Web Pages

To scrape dynamic web pages, Python Goose relies on a technique called "rendering." Rendering involves executing the JavaScript code on the web page to generate the dynamic content before extracting it.

Let's dive into some code to see how this works:

```python
from goose3 import Goose
from selenium import webdriver

# Configure Selenium web driver
driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://example.com")

# Get the dynamically loaded content
content = driver.page_source

# Initialize Python Goose
g = Goose()

# Extract the article from the web page
article = g.extract(raw_html=content)

# Access extracted data
title = article.title
text = article.cleaned_text

# Print the extracted data
print("Title:", title)
print("Text:", text)

# Close Selenium web driver
driver.quit()
```

In the above example, we first configure the Selenium web driver to open the desired web page. We then retrieve the dynamically loaded content using `driver.page_source`. Next, we initialize Python Goose and use the `extract()` method to extract the article from the web page. Finally, we can access the extracted data such as the title and text.

## Conclusion

In this article, we have explored how to scrape dynamic web pages using Python Goose. By using the rendering technique provided by Python Goose and the automation capabilities of Selenium, we can extract content from web pages that load their content dynamically using JavaScript. This opens up a whole new world of possibilities for web scraping. 

If you are interested in dynamic web scraping, give Python Goose a try and see how it can simplify the process for you.

#python #webscraping