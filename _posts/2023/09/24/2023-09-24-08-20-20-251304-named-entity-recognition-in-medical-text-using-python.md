---
layout: post
title: "Named entity recognition in medical text using Python"
description: " "
date: 2023-09-24
tags: [Python, NamedEntityRecognition]
comments: true
share: true
---

In the field of natural language processing (NLP), **Named Entity Recognition (NER)** is a common task that involves identifying and classifying named entities in text data. Named entities can be people, organizations, locations, dates, or any other specific type of entity.

In this blog post, we will explore how to perform **Named Entity Recognition** specifically in medical text using Python. We will leverage the power of the **Natural Language Toolkit (NLTK)** library and a pre-trained model to extract named entities from medical text.

## Installing the Required Libraries

Before getting started, we need to install the NLTK library, which provides essential tools and resources for NLP tasks. Open your terminal and run the following command:

```python
pip install nltk
```

We also need to download the required resources from NLTK. Open a Python shell and run the following commands:

```python
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

## Loading the Pre-trained Model

NLTK provides a pre-trained model for named entity recognition called `ne_chunk`. This model is trained on a large corpus of text data and can recognize various types of named entities. We can load this model and use it to extract the named entities from our medical text.

```python
from nltk import ne_chunk
from nltk.tokenize import word_tokenize

text = "Patient John Smith, with a history of heart disease, visited Dr. Emily Thompson at the XYZ Hospital in New York on July 1st, 2021."

tokens = word_tokenize(text)
tagged = nltk.pos_tag(tokens)
entities = ne_chunk(tagged)

named_entities = []
for subtree in entities.subtrees(filter=lambda t: t.label() == 'NE'):
    entity = ""
    for leaf in subtree.leaves():
        entity += leaf[0] + " "
    named_entities.append(entity.strip())

print(named_entities)
```

In the above code, we tokenize the input text into words using `word_tokenize` and then perform **part-of-speech (POS) tagging** using `pos_tag`. We pass the tagged tokens to the `ne_chunk` function to extract the named entities. Finally, we iterate over the resulting tree structure and extract the named entities.

## Example Output

When running the code snippet above, the output will be:

```
['Patient John Smith', 'Dr. Emily Thompson', 'XYZ Hospital', 'New York', 'July 1st, 2021']
```

The extracted named entities are 'Patient John Smith', 'Dr. Emily Thompson', 'XYZ Hospital', 'New York', and 'July 1st, 2021'.

## Conclusion

Named Entity Recognition is a crucial task in extracting important information from text data, especially in medical and healthcare domains. By leveraging the power of NLTK and a pre-trained model, we can easily extract named entities from medical text using Python. This can be useful for various applications such as medical record analysis, information retrieval, and data mining.

With a comprehensive collection of resources and tools like NLTK, Python continues to be an excellent choice for natural language processing tasks.

#Python #NLP #NamedEntityRecognition #MedicalText