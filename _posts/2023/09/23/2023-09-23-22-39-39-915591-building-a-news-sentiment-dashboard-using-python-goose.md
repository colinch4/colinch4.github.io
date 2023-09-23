---
layout: post
title: "Building a news sentiment dashboard using Python Goose"
description: " "
date: 2023-09-23
tags: [Goose, NewsSentiment]
comments: true
share: true
---

In this tutorial, we will learn how to build a news sentiment dashboard using Python and the **Goose** library. The dashboard will analyze news articles and provide sentiment analysis to determine whether the news is positive, negative, or neutral.

## What is Goose?

**Goose** is a Python library that allows us to extract content from news articles. It scrapes the HTML of a web page and identifies the relevant main text, removing ads, navigation menus, and other noise. This makes it a perfect tool for extracting news articles.

## Prerequisites

In order to follow along with this tutorial, you will need the following:

- Python installed on your machine (version 3 and above)
- The following Python libraries: Goose, NLTK, TextBlob, Pandas, and Matplotlib
- An API key from News API (a free account is sufficient)

## Step 1: Installation

First, you need to install the **Goose** library. Open your command prompt or terminal and enter the following command:

```python
pip install goose3
```

Next, install the other required libraries: **NLTK**, **TextBlob**, **Pandas**, and **Matplotlib** using the following commands:

```python
pip install nltk
pip install textblob
pip install pandas
pip install matplotlib
```

## Step 2: Importing the Required Libraries

Open your Python IDE or editor and import the necessary libraries:

```python
import nltk
from goose3 import Goose
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
```

## Step 3: Extracting News Articles

To scrape news articles, we need to provide the URL of the news article. We will use the **Goose** library to extract the main text from each article.

```python
g = Goose()
article_link = "https://www.example.com/article"
article = g.extract(url=article_link)

article_text = article.cleaned_text
```

## Step 4: Sentiment Analysis

Once we have extracted the news article's text, we can perform sentiment analysis using the **TextBlob** library. 

```python
blob = TextBlob(article_text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

if polarity > 0:
    sentiment = "positive"
elif polarity < 0:
    sentiment = "negative"
else:
    sentiment = "neutral"
```

## Step 5: Visualization

To visualize the sentiment analysis results, we will use the **Pandas** and **Matplotlib** libraries.

```python
data = {'Sentiment': ['Positive', 'Negative', 'Neutral'], 'Count': [positive_count, negative_count, neutral_count]}
df = pd.DataFrame(data)

plt.bar(df['Sentiment'], df['Count'])
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('News Sentiment Analysis')
plt.show()
```

## Conclusion

In this tutorial, we have learned how to build a news sentiment dashboard using Python and the Goose library. We have seen how to extract news articles, perform sentiment analysis, and visualize the results. This dashboard can be a valuable tool for analyzing public perception of certain news topics.

Don't forget to add `#Goose #NewsSentiment` to your posts when sharing them on social media.