---
layout: post
title: "Stemming and lemmatization in NLP using python"
description: " "
date: 2023-09-17
tags: []
comments: true
share: true
---

Natural Language Processing (NLP) is a field of study focused on making computers understand and process human language. One of the key challenges in NLP is dealing with the various forms of words that exist in a language. Stemming and Lemmatization are two techniques commonly used to address this challenge by reducing words to their base or root forms. In this blog post, we will explore how to perform stemming and lemmatization in Python using popular NLP libraries.

## Stemming
Stemming is the process of reducing words to their base or root form, often achieved by removing suffixes or endings. For example, the stem of the words "running", "runs", and "runner" is "run". Stemming is a simple rule-based approach that is computationally efficient but can sometimes produce incorrect stems.

Python provides several stemming libraries such as **NLTK** (Natural Language Toolkit) and **Stemming** which have different algorithms like PorterStemmer, LancasterStemmer, and SnowballStemmer. Let's see an example using the PorterStemmer algorithm from the NLTK library:

```python
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
word = "running"
stemmed_word = stemmer.stem(word)

print(stemmed_word)  # Output: run
```

## Lemmatization
Lemmatization is the process of reducing words to their base or dictionary form. Unlike stemming, lemmatization considers the context and part of speech of a word. For example, the lemma of words like "am", "are", and "is" is "be". Lemmatization produces more accurate results but is computationally more expensive compared to stemming.

The NLTK library also provides lemmatization functionality. Let's take a look at an example:

```python
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
word = "running"
pos = "v"  # 'v' indicates verb

lemmatized_word = lemmatizer.lemmatize(word, pos)

print(lemmatized_word)  # Output: run
```

In the above example, we specify the part of speech as a verb (`v`) for the word "running". This ensures that the lemmatization algorithm correctly interprets the word in the context of its usage and produces the expected lemma.

## Conclusion
Stemming and lemmatization are valuable techniques in Natural Language Processing to normalize words and reduce their various forms to a standard base or root form. While stemming is a simple and fast approach, lemmatization produces more accurate results by considering the context and part of speech. Depending on your NLP task, you can choose the appropriate technique accordingly.

#NLP #Python