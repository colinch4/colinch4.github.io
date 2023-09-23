---
layout: post
title: "Applying data visualization techniques on extracted articles with Python Goose"
description: " "
date: 2023-09-23
tags: []
comments: true
share: true
---

Data visualization is a powerful way to understand and communicate information from large datasets. In this blog post, we will explore how to apply data visualization techniques on extracted articles using the Python library, Goose.

Goose is a web scraping and article extraction library, which allows us to extract clean, formatted text content from web pages. With the extracted articles, we can then analyze and visualize the data using various Python libraries such as Matplotlib and Seaborn.

## Step 1: Installing Goose Library
Before we can start extracting articles, we need to install the Goose library. You can install it using pip with the following command:

```python
pip install goose3
```

## Step 2: Extracting Articles with Goose
To extract articles using Goose, we need to provide a URL of the web page containing the article. Here's an example of how to use Goose to extract articles:

```python
from goose3 import Goose

url = "https://www.example.com/article"
g = Goose()
article = g.extract(url)

article_title = article.title
article_text = article.cleaned_text

print(f"Title: {article_title}")
print(f"Text: {article_text}")
```

In the above example, we instantiate a Goose object and use its `extract()` method to extract the article from the given URL. We can then access the article's title and cleaned text using the `title` and `cleaned_text` attributes, respectively.

## Step 3: Analyzing the Extracted Articles
Once we have extracted the articles, we can perform various analyses on the data. For example, we can count the number of words in each article, identify the most frequent words, or even perform sentiment analysis.

For simplicity, let's count the number of words in each article using the `split()` method and visualize the results using a bar chart with Matplotlib.

```python
import matplotlib.pyplot as plt

article_urls = ["https://www.example.com/article1",
                "https://www.example.com/article2",
                "https://www.example.com/article3"]

word_counts = []
for url in article_urls:
    article = g.extract(url)
    word_count = len(article.cleaned_text.split())
    word_counts.append(word_count)

plt.bar(range(len(article_urls)), word_counts)
plt.xticks(range(len(article_urls)), [f"Article {i+1}" for i in range(len(article_urls))])
plt.xlabel("Articles")
plt.ylabel("Word Count")
plt.title("Word Count of Extracted Articles")
plt.show()
```

In the above example, we iterate over the list of article URLs, extract each article, and count the number of words using the `split()` method. We then store the word counts in a list. Afterward, we use Matplotlib to create a bar chart, visualizing the word counts for each article.

## Conclusion
In this blog post, we have explored how to apply data visualization techniques on extracted articles using the Python Goose library. We learned how to extract articles from web pages, analyze the extracted data, and visualize the results using Matplotlib. Data visualization can help us gain insights and effectively communicate information from large datasets.