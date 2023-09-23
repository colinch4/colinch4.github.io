---
layout: post
title: "Extracting articles for data journalism and investigative reporting using Python Goose"
description: " "
date: 2023-09-23
tags: [datajournalism, investigativereporting]
comments: true
share: true
---

In the world of data journalism and investigative reporting, extracting articles from websites is a common and important task. One popular tool for extracting article content is Python Goose. In this blog post, we will explore how to use Python Goose to extract articles for data journalism and investigative reporting.

## What is Python Goose?

Python Goose is a Python library that enables the extraction of article text and metadata from web pages. It uses machine learning algorithms to identify and extract the main content of an article while filtering out irrelevant information such as advertisements, headers, and footers.

## Getting started with Python Goose

Before we can start using Python Goose, we need to install it. You can install Python Goose using pip by running the following command:

```bash
pip install goose3
```

Once Python Goose is installed, we can start using it in our Python code. First, we need to import the library:

```python
import goose3
```

Next, we need to create an instance of the `Goose` class:

```python
g = goose3.Goose()
```

Now, we are ready to extract articles from web pages. To extract an article, we need to pass the URL of the web page to the `extract` method:

```python
url = "https://www.example.com/article"
article = g.extract(url)
```

The `article` object contains the extracted content and metadata of the article. We can access the title, published date, authors, and the main text of the article using the following attributes:

```python
title = article.title
published_date = article.publish_date
authors = article.authors
text = article.cleaned_text
```

## Additional features

Python Goose provides additional features to enhance the extraction process. For example, you can specify the language of the article to improve the extraction accuracy:

```python
article = g.extract(url, target_language='en')
```

You can also specify a custom parser to handle web pages with non-standard HTML structure:

```python
from goose3.configuration import Configuration

config = Configuration()
config.parser_class = 'myparser.MyParser'

g = goose3.Goose(config=config)
```

## Conclusion

Python Goose is a powerful tool for extracting articles for data journalism and investigative reporting. Its ability to identify and extract the main content of an article makes it a valuable asset in the field. By incorporating Python Goose into your data extraction workflow, you can save time and effort in gathering relevant articles for your projects.

#datajournalism #investigativereporting