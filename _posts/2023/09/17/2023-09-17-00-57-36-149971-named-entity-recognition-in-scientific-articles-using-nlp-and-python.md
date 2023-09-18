---
layout: post
title: "Named Entity Recognition in scientific articles using NLP and python"
description: " "
date: 2023-09-17
tags: [NamedEntityRecognition, ScientificArticles]
comments: true
share: true
---

Named Entity Recognition (NER) is a crucial task in Natural Language Processing (NLP) that involves identifying and classifying named entities in text into predefined categories such as person names, organizations, locations, medical terms, etc. NER is particularly useful when analyzing scientific articles as it allows researchers to extract valuable information such as mentions of genes, proteins, diseases, and other relevant entities.

In this blog post, we will explore how to perform Named Entity Recognition in scientific articles using Python and NLP libraries. Specifically, we will demonstrate the usage of the popular NLP library **spaCy** for this task.

## Installing spaCy
To start, we need to install spaCy and download its English language model. Open your terminal and execute the following command:

```
$ pip install spacy
$ python -m spacy download en_core_web_sm
```

## Loading the Scientific Article
Before performing NER, we need to load the scientific article into memory. For this demonstration, let's assume we have a text file named `article.txt` containing the scientific article. We can load it as follows:

```python
with open('article.txt', 'r') as file:
    article_text = file.read()
```

## Performing Named Entity Recognition
Now that our article is loaded, we can use spaCy to perform NER. The first step is to load the English language model we downloaded earlier:

```python
import spacy

nlp = spacy.load('en_core_web_sm')
```

Next, we can pass the article text to the `nlp` object to obtain a processed `Doc` object:

```python
doc = nlp(article_text)
```

Now, we can iterate over each token in the document and check if it is a named entity:

```python
for token in doc:
    if token.ent_type_:
        print(f"Entity: {token.text}, Type: {token.ent_type_}")
```

The `ent_type_` attribute provides the entity type for each token, and we can access the entity text using the `text` attribute.

## Extracting and Analyzing the Entities
We can collect the identified entities from the article into a list for further analysis or processing. Let's create a list named `entities` and populate it with the identified entities:

```python
entities = []

for token in doc:
    if token.ent_type_:
        entities.append({
            'entity': token.text,
            'type': token.ent_type_
        })
```

Now we have a list of entities, where each entity is a dictionary containing the entity text and its type.

## Conclusion
Named Entity Recognition is a powerful technique that can be used to extract valuable information from scientific articles. In this blog post, we demonstrated how to perform NER using spaCy and Python. By identifying and classifying entities, researchers can gain deeper insights and facilitate various natural language processing tasks in the domain of scientific research.

Give it a try on your own scientific articles and unleash the power of NER in your research!

#Python #NLP #NamedEntityRecognition #ScientificArticles