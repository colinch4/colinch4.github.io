---
layout: post
title: "Named entity recognition in biomedical text using Python"
description: " "
date: 2023-09-24
tags: [biomedical]
comments: true
share: true
---

Named Entity Recognition (NER) is a common task in natural language processing (NLP) that involves identifying and classifying named entities in text. In the biomedical domain, NER plays a crucial role in extracting important information from scientific papers, electronic health records, and other medical documents.

In this blog post, we will explore how to perform Named Entity Recognition in biomedical text using Python. Specifically, we will be using the popular NLP library, spaCy, along with a pre-trained model for biomedical text.

## Installing spaCy

To get started, we need to install the spaCy library. You can install it by running the following command:

`pip install spacy`

After installing spaCy, we need to download and install a pre-trained model specifically designed for biomedical text.

## Downloading the Pre-trained Model

spaCy provides various pre-trained models for different languages and domains. For biomedical text, we will be using the `en_ner_bionlp13cg_md` model. You can download it by running the following command:

`python -m spacy download en_ner_bionlp13cg_md`

## Performing Named Entity Recognition

With the model and spaCy installed, we can now perform Named Entity Recognition on biomedical text. The following code demonstrates how to do this:

```python
import spacy

# Load the pre-trained biomedical model
nlp = spacy.load("en_ner_bionlp13cg_md")

# Sample text for NER
text = "A recent study conducted at XYZ University demonstrated the efficacy of drug X in treating cancer."

# Apply NER on the text
doc = nlp(text)

# Extract named entities
entities = []
for entity in doc.ents:
    entities.append((entity.text, entity.label_))

# Print the named entities
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
```

In the above code, we first load the pre-trained `en_ner_bionlp13cg_md` model using the spaCy library. We then provide a sample text that we want to perform NER on. The `nlp` function applies NER on the text, and we can access the named entities using the `ents` property of the `doc` object.

Finally, we iterate over the named entities and print their text and corresponding label.

## Conclusion

In this blog post, we have learned how to perform Named Entity Recognition in biomedical text using Python and the spaCy library. By leveraging pre-trained models specifically designed for the biomedical domain, we can accurately identify and classify named entities in scientific literature and medical documents. Incorporating NER into various applications can help automate information extraction and advance research in the field of biomedicine.

#python #biomedical #textmining #namedentityrecognition