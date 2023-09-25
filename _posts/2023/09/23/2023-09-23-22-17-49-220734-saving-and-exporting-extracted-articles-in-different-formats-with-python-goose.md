---
layout: post
title: "Saving and exporting extracted articles in different formats with Python Goose"
description: " "
date: 2023-09-23
tags: [WebScraping]
comments: true
share: true
---

In this blog post, we will explore how to save and export extracted articles in different formats using Python and the Goose library. Goose is a Python library used for extracting and parsing articles from websites.

## Installation

Before we start, let's make sure we have Goose library installed. Run the following command to install it using pip:

```
pip install goose3
```

## Extracting Article Contents with Goose

To extract the content of an article from a website, we first need to install the Goose library. Once installed, we can use it to fetch and extract the content of a specific article with just a few lines of code.

Here's an example of how to extract the contents of an article:

```python
from goose3 import Goose

url = "https://example.com/article"  # URL of the article you want to extract
g = Goose()
article = g.extract(url)

title = article.title
text = article.cleaned_text

print("Title:", title)
print("Content:", text)
```

In this code snippet, we create an instance of the Goose class and pass it the URL of the article we want to extract. We then call the `extract()` method, which returns an Article object containing the extracted content. We can access the title and cleaned text of the article using the `title` and `cleaned_text` attributes, respectively.

Note: It's important to ensure that you have proper permission to scrape and extract content from the website you are targeting.

## Saving Articles in Different Formats

Now that we have extracted the article content, let's explore how to save it in different formats such as plain text, HTML, or PDF.

### Saving as Plain Text

To save the extracted article as plain text, we can simply write the contents to a text file using Python's `open()` function.

```python
filename = "article.txt"

with open(filename, "w") as file:
    file.write(text)

print("Article saved as plain text:", filename)
```

In this code snippet, we open a file with the specified `filename` in write mode ('w') and use the `write()` method to write the extracted text content to the file.

### Saving as HTML

If you want to save the extracted article as HTML, you can use the same approach but write the cleaned HTML content instead.

```python
filename = "article.html"

with open(filename, "w") as file:
    file.write(article.raw_html)

print("Article saved as HTML:", filename)
```

In the example above, we write the `raw_html` attribute of the `article` object to the file, which contains the cleaned HTML content of the extracted article.

### Saving as PDF

To save the extracted article as a PDF file, we can use external libraries such as `pdfkit` or `weasyprint` to convert the HTML content to PDF format.

Here's an example using `pdfkit`:

```python
import pdfkit

filename = "article.pdf"

pdfkit.from_string(article.raw_html, filename)

print("Article saved as PDF:", filename)
```

In this code snippet, we use the `from_string()` method from the `pdfkit` library to convert the HTML content (`article.raw_html`) to a PDF file.

## Conclusion

In this blog post, we explored how to save and export extracted articles in different formats using Python Goose. We learned how to extract article contents using the Goose library and save them as plain text, HTML, or PDF files. This can be beneficial for various applications, such as building a web scraper, conducting research, or archiving articles. 

#Python #WebScraping