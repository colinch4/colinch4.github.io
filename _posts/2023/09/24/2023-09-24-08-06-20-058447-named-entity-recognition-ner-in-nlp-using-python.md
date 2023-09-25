---
layout: post
title: "Named entity recognition (NER) in NLP using Python"
description: " "
date: 2023-09-24
tags: []
comments: true
share: true
---

## What is Named Entity Recognition?

Named Entity Recognition (NER) is a subtask of information extraction that aims to identify and classify named entities in text into predefined categories. These named entities can be names of people, organizations, locations, dates, etc. NER plays a significant role in various NLP applications, including question answering, information retrieval, and sentiment analysis.

## NER using Python

Python provides several libraries and tools that can be used to perform Named Entity Recognition efficiently. One such popular library is the Natural Language Toolkit (NLTK). NLTK is a powerful library for NLP tasks and provides pre-trained models and tools for NER.

To begin with, make sure you have NLTK installed. You can install NLTK by running the following command:

```python
pip install nltk
```

Once NLTK is installed, you can import it and download the required NER corpus as shown below:

```python
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

Now, let's see how we can perform Named Entity Recognition using NLTK:

```python
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize

def ner(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged = pos_tag(tokens)
    
    # Perform named entity recognition
    ne = ne_chunk(tagged)
    
    return ne

# Example usage
text = "Apple Inc. was founded in 1976 by Steve Jobs and Steve Wozniak."
entities = ner(text)
print(entities)
```

In the above code snippet, we first tokenize the input text using `word_tokenize` from NLTK. Then, we perform part-of-speech tagging using `pos_tag` to assign a grammatical category to each token. Finally, we apply named entity recognition using `ne_chunk` to identify and classify the named entities in the text.

The output of the code snippet will be:

```
(S
  (ORGANIZATION Apple/NNP Inc./NNP)
  was/VBD
  founded/VBN
  in/IN
  1976/CD
  by/IN
  (PERSON Steve/NNP Jobs/NNP)
  and/CC
  (PERSON Steve/NNP Wozniak/NNP)
  ./.)
```

Here, `(ORGANIZATION Apple Inc.)` represents the identified organization entity, and `(PERSON Steve Jobs)` and `(PERSON Steve Wozniak)` represent the identified person entities.

## Conclusion

Named Entity Recognition (NER) is a crucial task in NLP that involves identifying and classifying named entities in text. In this blog post, we explored how to perform NER using Python and the NLTK library. NER can be used in various real-world applications to extract valuable information from text data. By leveraging Python's powerful NLP libraries, you can easily incorporate NER capabilities into your own projects. Start exploring the world of named entities with NER and unlock the potential of your text data!

#Python #NLP