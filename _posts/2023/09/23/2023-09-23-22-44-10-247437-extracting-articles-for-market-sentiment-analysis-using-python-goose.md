---
layout: post
title: "Extracting articles for market sentiment analysis using Python Goose"
description: " "
date: 2023-09-23
tags: [python, sentimentanalysis]
comments: true
share: true
---

## What is Goose?

Goose is a Python library specifically designed for article extraction from web pages. It uses a smart algorithm to extract the main content of an article from the clutter of advertisements, navigation menus, and other irrelevant information typically found on web pages.

## Installation

To start using Goose, we need to install the library. Open your terminal or command prompt and run the following command:

```python
pip install goose3
```

## Extracting Articles

Once Goose is installed, we can start extracting articles. First, we need to import the Goose class from the `goose3` module:

```python
from goose3 import Goose
```

Next, we create an instance of the Goose class:

```python
g = Goose()
```

Now we're ready to extract articles. We need to pass the URL of the web page that contains the article we want to extract. Let's extract an article from the BBC News website:

```python
url = 'https://www.bbc.com/news/business-12345678'
article = g.extract(url=url)
```

The `extract()` method returns an Article object that contains various attributes like title, description, publish date, and article text. We can access these attributes using dot notation:

```python
print(article.title)  # Print the title of the article
print(article.publish_date)  # Print the publish date of the article
print(article.cleaned_text)  # Print the cleaned text of the article
```

## Sentiment Analysis

Now that we have extracted the article, we can perform sentiment analysis on its text. There are several Python libraries available for sentiment analysis, such as NLTK and TextBlob. For the purpose of this blog post, let's use TextBlob.

First, make sure you have installed TextBlob by running the following command:

```python
pip install textblob
```

Then, import the TextBlob class:

```python
from textblob import TextBlob
```

To perform sentiment analysis on the article text, create a TextBlob object and call its `sentiment` property:

```python
blob = TextBlob(article.cleaned_text)
sentiment = blob.sentiment
```

The `sentiment` property returns a named tuple with two attributes: `polarity` and `subjectivity`. Polarity represents the sentiment (-1 to 1, where negative values indicate negative sentiment and positive values indicate positive sentiment), and subjectivity represents the subjectivity of the text (0 to 1, where 0 indicates objective and 1 indicates subjective).

## Conclusion

Analyzing market sentiment can provide valuable insights for making investment decisions. Python Goose is a powerful library that allows us to extract articles from web pages, and combined with sentiment analysis techniques, we can get a better understanding of market sentiment. In this blog post, we explored how to use Goose to extract articles and perform sentiment analysis. By leveraging these techniques, we can uncover hidden patterns and trends that can be invaluable in the financial world.

#python #sentimentanalysis #gooselibrary