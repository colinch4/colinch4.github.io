---
layout: post
title: "Named Entity Recognition (NER) in NLP using Python"
description: " "
date: 2023-09-24
tags: []
comments: true
share: true
---

Named Entity Recognition (NER) is a subtask of Natural Language Processing (NLP) that aims to identify and classify named entities in a text into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

NER is useful in various applications like information extraction, question answering systems, machine translation, sentiment analysis, chatbots, and more.

In this blog post, we will explore how to perform NER using Python and the Natural Language Toolkit (NLTK) library.

## Installing the Required Libraries
First, let's install the NLTK library, if you don't have it already. Open your terminal and run the following command:

```python
pip install nltk
```

You also need to download the necessary resources for NER. Open a Python shell and run the following code:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

## Tokenization and Part-of-Speech Tagging
Before performing NER, we need to tokenize the text into words and then assign part-of-speech (POS) tags to each word. The POS tags help in determining the grammatical category of a word, which is useful in the NER process.

```python
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(text):
    tokens = word_tokenize(text)
    # Assign POS tags to the words
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens

text = "Steve Jobs co-founded Apple Inc. in 1976."
tagged_tokens = preprocess(text)
print(tagged_tokens)
```

## Performing Named Entity Recognition
To perform NER, we will use the named entity chunker provided by NLTK. It uses a pre-trained model to identify named entities in a text.

```python
from nltk import ne_chunk

def ner(text):
    tagged_tokens = preprocess(text)
    # Apply named entity chunking
    entities = ne_chunk(tagged_tokens)
    return entities

text = "Steve Jobs co-founded Apple Inc. in 1976."
entities = ner(text)
print(entities)
```

## Entity Classification
The entities detected by the NER process are typically in the form of nested tree structures. We can traverse this tree and extract the named entities along with their corresponding categories.

```python
def get_entities(tree):
    entities = []
    if hasattr(tree, 'label') and tree.label:
        if tree.label() == 'NE':
            entities.append(' '.join([child[0] for child in tree]))
        else:
            for child in tree:
                entities.extend(get_entities(child))
    return entities

entities_list = get_entities(entities)
print(entities_list)
```

## Conclusion
In this blog post, we learned how to perform Named Entity Recognition (NER) using Python and the NLTK library. NER is a crucial step in various NLP applications where identifying and classifying named entities is essential. By leveraging NER, we can extract valuable information from unstructured text data.