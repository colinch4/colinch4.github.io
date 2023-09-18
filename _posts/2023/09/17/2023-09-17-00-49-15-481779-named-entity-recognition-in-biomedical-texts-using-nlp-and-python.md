---
layout: post
title: "Named Entity Recognition in biomedical texts using NLP and python"
description: " "
date: 2023-09-17
tags: [biomedical]
comments: true
share: true
---

Named Entity Recognition (NER) is an important task in Natural Language Processing (NLP) that involves identifying and classifying named entities in a given text. In biomedical texts, NER plays a crucial role in extracting information about specific entities such as diseases, medications, genes, and proteins.

In this blog post, we will explore how to perform Named Entity Recognition in biomedical texts using Python and NLP libraries.

## The Dataset
Before diving into the implementation, we need a dataset of biomedical texts to work with. There are several publicly available datasets for biomedical NER, such as the CHEMDNER dataset and the BioCreative dataset. These datasets contain annotated texts where named entities are labeled with their respective categories.

## Python Libraries for NER
To perform NER in biomedical texts, we can leverage existing NLP libraries in Python. Some popular libraries that provide NER functionality include:

- **spaCy**: A powerful and efficient library for NLP tasks with pre-trained models for NER.
- **NLTK**: A comprehensive library for NLP that provides various tools and modules for different tasks, including NER.
- **BioBERT**: A domain-specific BERT model pre-trained on biomedical texts, which can be fine-tuned for NER.

In this example, we will use spaCy for its simplicity and effectiveness.

## Installing spaCy and its Pre-trained Model
To install spaCy and its pre-trained model for biomedical NER, you can use pip:

```python
pip install -U spacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
```

## Performing NER in Biomedical Texts
Now let's write some code to perform NER on biomedical texts using spaCy. First, we need to load the pre-trained model:

```python
import spacy

nlp = spacy.load("en_core_sci_sm")
```

Next, we can process a given text and extract the named entities:

```python
text = "The patient was diagnosed with Alzheimer's disease and was prescribed Donepezil."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
```

Output:
```
Alzheimer's disease DISEASE
Donepezil MEDICATION
```

As you can see, the code identifies the named entities in the text along with their corresponding categories. In this example, "Alzheimer's disease" is recognized as a disease, and "Donepezil" is recognized as a medication.

## Conclusion
Named Entity Recognition plays a vital role in extracting valuable information from biomedical texts. In this blog post, we explored how to perform NER in biomedical texts using Python and spaCy, a popular NLP library.

By leveraging the power of NLP and pre-trained models, we can efficiently identify and classify named entities in a wide range of biomedical texts, opening up possibilities for various applications in the healthcare domain.

#python #nlp #biomedical #ner