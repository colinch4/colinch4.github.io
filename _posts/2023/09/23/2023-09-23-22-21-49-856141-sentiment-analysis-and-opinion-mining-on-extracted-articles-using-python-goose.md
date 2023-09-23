---
layout: post
title: "Sentiment analysis and opinion mining on extracted articles using Python Goose"
description: " "
date: 2023-09-23
tags: [dataanalysis, sentimentanalysis]
comments: true
share: true
---

In the era of big data, extracting and analyzing textual data is becoming increasingly important. One popular use case is sentiment analysis and opinion mining, which involves identifying and categorizing the sentiment or opinion expressed in a piece of text.

In this blog post, we will explore how to perform sentiment analysis and opinion mining on extracted articles using Python Goose, a powerful library for extracting textual content from websites.

## What is Python Goose?

Python Goose is a well-known Python library that allows us to extract textual content and metadata from web pages. It uses machine learning algorithms to extract relevant information and discard irrelevant content such as advertisements and navigation menus.

To get started, we need to install Python Goose using `pip`. Open your terminal and run the following command:

```python
pip install goose3
```

## Extracting Article Text using Python Goose

Once we have Python Goose installed, we can start extracting articles from websites. Let's assume we have a list of URLs pointing to different articles. Here's how we can extract the article text:

```python
from goose3 import Goose

# Create a Goose instance
g = Goose()

# List of article URLs
article_urls = [
    "https://example.com/article1",
    "https://example.com/article2",
    "https://example.com/article3"
]

# Loop through the URLs and extract the article text
for url in article_urls:
    # Load the article
    article = g.extract(url=url)

    # Print the article text
    print(article.cleaned_text)
```

## Performing Sentiment Analysis

Now that we have extracted the article text, let's move on to performing sentiment analysis. There are various libraries and techniques available for sentiment analysis, but for simplicity, we will use the AFINN-111 wordlist, which assigns pre-computed sentiment scores to words.

First, we need to install the `nltk` library, which provides an interface to the AFINN-111 wordlist. Run the following command in your terminal:

```python
pip install nltk
```

Next, we need to download the AFINN-111 wordlist. Open a Python shell and run the following commands:

```python
import nltk

nltk.download('afinn')
```

Once we have the wordlist, we can proceed with sentiment analysis:

```python
from afinn import Afinn

# Create an Afinn instance
afinn = Afinn()

# Sentiment analysis on each article
for url in article_urls:
    article = g.extract(url=url)
    text = article.cleaned_text

    # Calculate the sentiment score
    sentiment_score = afinn.score(text)

    # Print the sentiment score
    print(f"Sentiment score for {url}: {sentiment_score}")
```

The `sentiment_score` value can range from negative to positive, where negative values indicate negative sentiment and positive values indicate positive sentiment.

## Conclusion

In this blog post, we have explored how to extract article text using Python Goose and perform sentiment analysis using the AFINN-111 wordlist. This approach can be useful for analyzing customer feedback, social media posts, and other forms of textual data.

By incorporating sentiment analysis and opinion mining into your data analysis pipeline, you can gain valuable insights into public opinion and sentiment towards your business, products, or services.

#dataanalysis #sentimentanalysis