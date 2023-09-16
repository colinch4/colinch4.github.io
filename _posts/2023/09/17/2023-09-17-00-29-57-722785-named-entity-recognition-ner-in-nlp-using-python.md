---
layout: post
title: "Named Entity Recognition (NER) in NLP using python"
description: " "
date: 2023-09-17
tags: [python, namedentityrecognition, spacy]
comments: true
share: true
---

In Natural Language Processing (NLP), Named Entity Recognition (NER) is the process of identifying and classifying named entities in text into predefined categories such as person names, locations, organizations, time expressions, quantities, etc. NER plays a crucial role in various applications such as information retrieval, question answering, text summarization, and more.

Python provides several libraries and tools for performing NER, and in this blog post, we will explore one of the popular libraries called spaCy.

## Installing spaCy

To get started with spaCy, you first need to install it. You can use the **pip** package manager to install spaCy:

```bash
pip install -U spacy
```

You also need to download the appropriate language model for spaCy. For example, to download the English language model, you can use the following command:

```bash
python -m spacy download en_core_web_sm
```

## Using spaCy for NER

Once you have spaCy installed and the language model downloaded, you can start using it for NER. Here's an example code snippet that demonstrates how to use spaCy for NER:

```python
import spacy

# Load the language model
nlp = spacy.load('en_core_web_sm')

# Define the text
text = "Apple Inc. is planning to open a new store in New York City."

# Process the text with spaCy
doc = nlp(text)

# Print the named entities
for entity in doc.ents:
    print(entity.text, entity.label_)
```

In the above code, we load the English language model using `spacy.load('en_core_web_sm')`. Then, we define a text string that contains a sentence with a named entity. The text is processed using `nlp(text)` to obtain a `Doc` object. We can then iterate over the named entities in the document using `doc.ents`.

## Understanding the Named Entity Labels

When printing the named entities, we also print their corresponding labels using `entity.label_`. The labels represent the category/class of the named entity. Some common labels include:

- **PERSON**: People, including fictional characters.
- **ORG**: Companies, agencies, institutions, etc.
- **GPE**: Countries, cities, states.
- **DATE**: Absolute or relative dates or periods.
- **QUANTITY**: Measurements, weights, distances, etc.

For a complete list of all the available labels, you can refer to the spaCy documentation.

## Conclusion

Named Entity Recognition is an essential task in Natural Language Processing that helps in extracting valuable information from text. In this blog post, we explored how to use spaCy, a popular Python library, for performing NER. With its ease of use and extensive features, spaCy can be a powerful tool for working with NER tasks. So go ahead and give it a try in your next NLP project!

#python #nlp #namedentityrecognition #spacy