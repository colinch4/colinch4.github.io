---
layout: post
title: "Sentiment analysis on extracted articles using Python Goose"
description: " "
date: 2023-09-23
tags: [goose]
comments: true
share: true
---

In today's digital age, the internet is flooded with vast amounts of content in the form of articles, blog posts, news updates, etc. Analyzing the sentiment of these articles can provide valuable insights into the opinions and emotions expressed by the authors and help in understanding public sentiment towards various topics. Python Goose is a powerful library that enables article extraction and sentiment analysis with ease. In this blog post, we will explore how to use Python Goose to extract articles and perform sentiment analysis on the extracted content.

## What is Python Goose?

Python Goose is a lightweight and easy-to-use library for extracting article content from web pages. It leverages natural language processing techniques to extract the main body of an article along with its metadata such as title, author, publish date, etc. It provides a simple and intuitive API for parsing web pages and extracting article content in a structured manner.

## Installing Python Goose

To get started, we need to install Python Goose. You can install it using pip, the Python package manager, by running the following command:

```python
pip install goose3
```

## Extracting Articles with Python Goose

Once we have Python Goose installed, we can extract articles from web pages effortlessly. Here's a simple code snippet to extract the main content of an article using Python Goose:

```python
from goose3 import Goose

# Instantiate the Goose object
g = Goose()

# Define the URL of the article you want to extract
article_url = "https://example.com/article"

# Extract the article content
article = g.extract(url=article_url)

# Print the article title, author, publish date, and content
print("Title:", article.title)
print("Author:", article.author)
print("Publish Date:", article.publish_date)
print("Content:", article.cleaned_text)
```

In the above code, we first create an instance of the Goose object. Then, we provide the URL of the article we want to extract and call the `extract()` method to get the article content. We can then access various attributes of the article object like title, author, publish date, and content.

## Performing Sentiment Analysis on Extracted Articles

Once we have extracted the articles, we can utilize the power of natural language processing to gauge the sentiment expressed in the article. There are various open-source libraries available in Python, such as NLTK and TextBlob, that can be used for sentiment analysis. Let's use TextBlob for sentiment analysis in this example:

```python
from textblob import TextBlob

# Perform sentiment analysis on the extracted article content
sentiment = TextBlob(article.cleaned_text).sentiment

# Print the sentiment polarity and subjectivity
print("Sentiment Polarity:", sentiment.polarity)
print("Sentiment Subjectivity:", sentiment.subjectivity)
```

In the above code, we create a TextBlob object by passing the cleaned text of the extracted article. TextBlob provides a convenient `sentiment` property that calculates the sentiment polarity and subjectivity of the text. The sentiment polarity ranges from -1 (negative sentiment) to 1 (positive sentiment), and the subjectivity ranges from 0 (objective) to 1 (subjective).

## Conclusion

Python Goose is a versatile library for article extraction, and when combined with sentiment analysis libraries like TextBlob, it enables us to gain valuable insights from the articles available on the web. Whether it's for market research, media monitoring, or opinion mining, Python Goose empowers us to extract and analyze articles effectively. So go ahead, give it a try, and unlock the power of sentiment analysis on extracted articles!

#python #goose #sentimentanalysis #naturallanguageprocessing