---
layout: post
title: "Named Entity Recognition in medical texts using NLP and python"
description: " "
date: 2023-09-17
tags: [NamedEntityRecognition]
comments: true
share: true
---

With the exponential growth of medical research and literature, it has become increasingly important to extract key information from large volumes of text efficiently. Named Entity Recognition (NER) is a popular Natural Language Processing (NLP) technique that can automate the identification and classification of named entities in text data.

Named entities are words or phrases that refer to specific types of entities such as names of people, organizations, locations, and medical terminologies. NER in the medical domain can greatly assist in various tasks such as clinical entity recognition, drug discovery, and pharmacovigilance.

In this blog post, we will explore how to perform Named Entity Recognition in medical texts using NLP techniques and the Python programming language.

## 1. Preparing the Data

Before performing NER, we need to pre-process and clean the medical text data. This involves removing unnecessary characters, converting the text to lowercase, and tokenizing the text into individual words or phrases.

```python
import re
import nltk

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\W', ' ', text)   # Remove non-alphanumeric characters
    text = text.lower()               # Convert to lowercase
    return text

def tokenize_text(text):
    tokens = nltk.word_tokenize(text) # Tokenize text into words
    return tokens
```

## 2. Building a Named Entity Recognition Model

To build our NER model, we can leverage pre-trained models or train our own using annotated medical text data. For demonstration purposes, let's use the popular `spaCy` library in Python, which provides pre-trained models for named entity recognition.

```python
import spacy

def perform_ner(text):
    nlp = spacy.load("en_core_sci_md")  # Load pre-trained model
    doc = nlp(text)                     # Process the text
    entities = [(ent.text, ent.label_) for ent in doc.ents]  # Extract entities and their labels
    return entities
```

`spaCy` provides various pre-trained models, including models specifically trained on medical texts such as `en_core_sci_md` or `en_ner_bc5cdr_md`. These models have been trained on a large annotated medical text corpus, making them effective for medical NER tasks.

## 3. Visualizing the Named Entities

To better understand the identified named entities, we can visualize them using libraries such as `matplotlib` or `seaborn`. This can provide valuable insights into the distribution and types of entities present in the medical texts.

```python
import matplotlib.pyplot as plt

def visualize_entities(entities):
    entity_labels = [entity[1] for entity in entities]  # Extract entity labels
    entity_counts = {label: entity_labels.count(label) for label in set(entity_labels)}  # Count occurrences

    labels = list(entity_counts.keys())
    counts = list(entity_counts.values())

    plt.bar(labels, counts)
    plt.xlabel("Entity Labels")
    plt.ylabel("Counts")
    plt.title("Distribution of Named Entities")
    plt.show()
```

## Conclusion

Named Entity Recognition is a powerful technique for extracting important information from large volumes of medical texts. In this blog post, we explored how to perform NER in medical texts using NLP techniques and Python. We discussed data preparation, building a NER model using a pre-trained model, and visualizing the identified entities.

By leveraging NER, researchers, healthcare professionals, and organizations can efficiently extract valuable insights from medical texts, leading to advancements in healthcare and medical research.

#NLP #NamedEntityRecognition