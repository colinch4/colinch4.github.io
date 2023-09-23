---
layout: post
title: "Sentiment analysis in NLP using Python"
description: " "
date: 2023-09-24
tags: [NLTK, SentimentAnalysis]
comments: true
share: true
---
Sentiment analysis is a technique in Natural Language Processing (NLP) that aims to determine the sentiment or emotional tone behind a piece of text. In other words, it helps in identifying whether a given text is positive, negative, or neutral. It has numerous applications ranging from social media monitoring to customer feedback analysis.

In this blog post, we will explore how to perform sentiment analysis using Python. We will use the popular Natural Language Toolkit (NLTK) library, which provides several useful tools and resources for NLP.

## Installing NLTK
First, let's install the NLTK library by running the following command in your Python environment:

```python
pip install nltk
```

## Dataset Preparation
To demonstrate sentiment analysis, we need a dataset that contains labeled text with corresponding sentiment labels. NLTK provides a built-in dataset called "movie_reviews" that we can use for this purpose. We can download the dataset using the following code:

```python
import nltk

nltk.download('movie_reviews')
```

## Text Preprocessing
Before we can train a sentiment analysis model, we need to preprocess the text data. This involves removing unnecessary characters, converting text to lowercase, and tokenizing the text into individual words or tokens. NLTK provides several utilities to perform these tasks:

```python
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Load the movie reviews dataset
reviews = [(movie_reviews.raw(fileid), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

# Preprocess the text
lemmatizer = WordNetLemmatizer()

preprocessed_reviews = []

for review, label in reviews:
    tokens = word_tokenize(review.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    preprocessed_reviews.append((tokens, label))
```

## Building a Sentiment Analysis Model
Next, we can build a sentiment analysis model using the preprocessed reviews. Here, we will use a simple bag-of-words representation and a Naive Bayes classifier to classify the sentiment of a given text:

```python
import random
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# Split the data into training and testing sets
random.shuffle(preprocessed_reviews)
train_data = preprocessed_reviews[:1500]
test_data = preprocessed_reviews[1500:]

# Extract features from the preprocessed data
def extract_features(review_tokens):
    return dict([(token, True) for token in review_tokens])

train_features = [(extract_features(review), label) for (review, label) in train_data]
test_features = [(extract_features(review), label) for (review, label) in test_data]

# Train the Naive Bayes classifier
sentiment_classifier = NaiveBayesClassifier.train(train_features)

# Evaluate the classifier
accuracy_score = accuracy(sentiment_classifier, test_features)
print(f"Accuracy: {accuracy_score * 100:.2f}%")
```

## Conclusion
Sentiment analysis is a valuable technique in NLP that can be used to gain insights from textual data. In this blog post, we learned how to perform sentiment analysis using Python and the NLTK library. We covered the steps involved in preprocessing the text data and building a sentiment analysis model using the Naive Bayes classifier.

By applying sentiment analysis, we can analyze customer sentiments, track social media trends, and make data-driven decisions. This can be particularly useful in market research, brand monitoring, and customer satisfaction analysis.

#NLTK #SentimentAnalysis