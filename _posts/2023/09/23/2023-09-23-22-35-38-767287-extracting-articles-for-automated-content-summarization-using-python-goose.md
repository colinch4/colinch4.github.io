---
layout: post
title: "Extracting articles for automated content summarization using Python Goose"
description: " "
date: 2023-09-23
tags: [python, webscraping]
comments: true
share: true
---

In the age of information overload, extracting relevant and concise information from articles and web content has become crucial. Automated content summarization can help in processing large volumes of text and extracting the most important information. In this blog post, we will explore how to extract articles using Python Goose library and leverage it for automated content summarization.

## What is Goose?

Goose is a Python library that allows us to extract articles and their metadata from web pages. It uses a combination of machine learning and rule-based techniques to identify the main content of a web page and remove noise such as ads, sidebars, and navigation menus.

## Installation

To begin, we need to install Goose library. You can install it using pip by running the following command:

```python
pip install goose3
```

## Extracting Article Content

Once Goose is installed, we can start extracting articles from web pages. Here is an example code snippet to illustrate how to extract article content using Goose:

```python
from goose3 import Goose

url = "https://example.com/article-url"
g = Goose()
article = g.extract(url)

print(article.title)
print(article.cleaned_text)
```
In the above code, we first import the Goose class from the goose3 module. We provide the URL of the article we want to extract in the `url` variable. Then we initialize an instance of the Goose class and call the `extract()` method, passing the URL as a parameter. The `extract()` method returns an Article object that contains the extracted article content.

We can access various properties of the Article object such as `title` and `cleaned_text` to retrieve the extracted article's title and main content, respectively.

## Automated Content Summarization

Now that we have extracted the article content, we can utilize various techniques for automated content summarization. One popular approach is using **TextRank**, an algorithm based on Google's PageRank, which assigns importance scores to sentences based on their semantic similarity.

Here is an example code snippet using the `sumy` library to perform automatic summarization:

```python
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

parser = PlaintextParser.from_string(article.cleaned_text, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(document=parser.document, sentences_count=3)

for sentence in summary:
    print(sentence)
```
In the above code, we first import the necessary classes from the `sumy` library. We create a `PlaintextParser` object using the article's cleaned text and an English tokenizer. Then we initialize an instance of the `LexRankSummarizer` class. We pass the parsed document and the desired number of sentences for the summary to the `summarizer` method.

The `summarizer` method returns a list of `Sentence` objects representing the summary sentences. We iterate over the list and print each sentence to see the summary.

## Conclusion

Automated content summarization using Python Goose library makes it easy to extract articles from web pages. By combining it with techniques such as TextRank, we can generate concise and relevant summaries from extracted articles. This can be particularly useful for applications such as news aggregators, information retrieval systems, and content analysis. Start exploring the possibilities of automated content summarization today!

#python #webscraping