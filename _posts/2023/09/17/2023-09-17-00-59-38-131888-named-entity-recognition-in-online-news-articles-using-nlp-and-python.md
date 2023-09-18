---
layout: post
title: "Named Entity Recognition in online news articles using NLP and python"
description: " "
date: 2023-09-17
tags: []
comments: true
share: true
---

Named Entity Recognition (NER) is a critical task in Natural Language Processing (NLP) that involves identifying and classifying named entities in text. Entities can be anything from people, organizations, locations, dates, to various other types of specific terms.

In this blog post, we will explore how to perform Named Entity Recognition on online news articles using NLP techniques and the Python programming language.

## Why Named Entity Recognition is Important

Named Entity Recognition is important because it helps us extract valuable information from unstructured text data. By automatically identifying and categorizing named entities, we can gain insights into the who, what, and where of a given news article. This can be particularly useful for information extraction, sentiment analysis, summarization, and many other applications.

## Preparing the Environment

To get started, we need to set up a Python environment with the necessary libraries. We will be using the `spacy` library, a popular open-source NLP library for Python. Install it using pip:

```
pip install -U spacy
```

Next, download the English language model for `spacy`:

```
python -m spacy download en_core_web_sm
```

## Performing Named Entity Recognition

Now that we have the environment ready, let's dive into the code. First, we need to import the `spacy` library and load the English language model:

```python
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")
```

Next, we will define a function to perform Named Entity Recognition on a given text:

```python
def perform_ner(text):
    # Process the text with the loaded NLP model
    doc = nlp(text)
    
    # Iterate over the identified entities and print their text and labels
    for entity in doc.ents:
        print(entity.text, entity.label_)
```

Now, we can pass our news article text to the `perform_ner` function to extract the named entities:

```python
text = "Apple Inc. is planning to open a new store in New York City on January 1st, 2022."
perform_ner(text)
```

The output will be:

```
Apple Inc. ORG
New York City GPE
January 1st, 2022 DATE
```

## Conclusion

Named Entity Recognition is a powerful technique for automatically identifying and categorizing named entities in text. In this blog post, we have explored how to perform NER on online news articles using NLP techniques and Python. By extracting named entities, we can gain valuable insights and enable various downstream applications. Experiment with different news articles and see what entities you can uncover!

#NLP #Python