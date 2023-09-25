---
layout: post
title: "Building a personalized news feed using Python Goose"
description: " "
date: 2023-09-23
tags: [NewsFeed]
comments: true
share: true
---

In this post, we will explore how to build a personalized news feed using Python and the *Goose* library. This will allow us to scrape news articles from various sources and create a customized feed based on our preferences. 

## What is Python Goose?

*Python Goose* is a Python library that helps us extract clean and well-structured article content from online news sources. It takes in a URL as input and returns the content of the article in a format that is easy to parse and analyze.

## Getting Started

To get started, we need to install *Python Goose*. We can do this by running the following command in our terminal:

```python
pip install goose3
```

Once we have *Python Goose* installed, we can import it in our Python script:

```python
from goose3 import Goose
```

## Scraping News Articles

To scrape a news article using *Python Goose*, we need to create an instance of the `Goose` class and pass in the URL of the article we want to scrape:

```python
url = "https://example.com/news/article"
g = Goose()
article = g.extract(url=url)
```

The `extract()` method returns an `Article` object that contains the title, author, publish date, and the actual content of the article.

## Building a Personalized News Feed

To build a personalized news feed, we can create a list of news sources and retrieve articles from each source. For example, let's say we have a list of URLs of news sources:

```python
news_sources = [
    "https://example.com/news/source1",
    "https://example.com/news/source2",
    "https://example.com/news/source3"
]
```

We can then iterate over the `news_sources` list, scrape the articles using *Python Goose*, and store them in a data structure such as a list or a database:

```python
articles = []
for source in news_sources:
    article = g.extract(url=source)
    articles.append(article)
```

Finally, we can sort the articles based on our preferences and display them in our personalized news feed.

## Conclusion

In this post, we have explored how to build a personalized news feed using Python and the *Goose* library. We learned how to scrape news articles from various sources and create a customized feed based on our preferences. With this knowledge, you can now create your own personalized news feed and stay up to date with the latest news from your favorite sources.

*#Python #NewsFeed*