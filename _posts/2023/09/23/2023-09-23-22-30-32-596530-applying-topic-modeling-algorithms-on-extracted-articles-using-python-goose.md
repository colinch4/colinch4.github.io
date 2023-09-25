---
layout: post
title: "Applying topic modeling algorithms on extracted articles using Python Goose"
description: " "
date: 2023-09-23
tags: [WebScraping]
comments: true
share: true
---

In this blog post, we will explore the process of applying topic modeling algorithms on extracted articles using the Python library called Goose. Topic modeling is a technique used to identify the main themes or topics in a collection of documents.

## What is Python Goose?

Python Goose is a web scraping and content extraction library. It allows us to easily extract clean and structured content from articles, blog posts, and news websites. One of its main applications is to scrape articles for further analysis, such as topic modeling.

## Extracting Articles using Python Goose

To begin with, we need to install the Python Goose library. You can do this by running the following command:

```python
pip install goose3
```

Once installed, we can use Python Goose to extract articles from a given URL. Here's an example of how to extract an article using Python Goose:

```python
from goose3 import Goose

url = 'https://example.com/article'
g = Goose()
article = g.extract(url)

print(article.title)
print(article.cleaned_text)
```

In the above example, we create a Goose object, pass the URL of the article we want to extract, and call the `extract()` method. The extracted article is then stored in the `article` variable, and we can access its title and cleaned text.

## Preprocessing the Extracted Articles

Before applying topic modeling algorithms, it's important to preprocess the extracted articles. Preprocessing involves removing stop words, punctuation, and special characters, as well as tokenizing the text into individual words.

Here's an example of how to preprocess the cleaned text of the extracted article using the NLTK library in Python:

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove punctuation and special characters
    tokens = [token.lower() for token in tokens if token.isalpha()]

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

preprocessed_text = preprocess_text(article.cleaned_text)

print(preprocessed_text)
```

In the above example, we import the necessary libraries from NLTK and download the required resources. We define a function called `preprocess_text()` that takes the cleaned text as input, tokenizes the text, removes punctuation and special characters, removes stop words, and lemmatizes the tokens. The preprocessed text is then stored in the `preprocessed_text` variable.

## Applying Topic Modeling Algorithms

Now that we have preprocessed the extracted articles, we can apply various topic modeling algorithms to identify the main topics. One popular topic modeling algorithm is Latent Dirichlet Allocation (LDA), which is available in the Gensim library.

Here's an example of how to apply LDA on the preprocessed text using Gensim in Python:

```python
from gensim import corpora, models

# Create a dictionary from the preprocessed text
dictionary = corpora.Dictionary([preprocessed_text])

# Create a corpus from the dictionary
corpus = [dictionary.doc2bow(text) for text in [preprocessed_text]]

# Apply LDA on the corpus
lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Print the topics
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))
```

In the above example, we create a dictionary from the preprocessed text, then create a corpus from the dictionary. We then apply LDA on the corpus by specifying the number of topics and the number of passes. Finally, we print the topics identified by the LDA model.

## Conclusion

In this blog post, we have explored the process of applying topic modeling algorithms on extracted articles using Python Goose. We have learned how to extract articles using Python Goose, preprocess the extracted articles, and apply topic modeling algorithms such as LDA to identify the main topics. By leveraging these techniques, we can gain valuable insights from a collection of articles and better understand the underlying themes or topics within them.

#Python #WebScraping #TopicModeling #PythonGoose