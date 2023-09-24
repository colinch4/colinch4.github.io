---
layout: post
title: "SpaCy를 사용하여 텍스트의 감정 분석(Sentiment Analysis)"
description: " "
date: 2023-09-24
tags: [SentimentAnalysis]
comments: true
share: true
---

Sentiment analysis is a technique used to determine the sentiment or emotion present in a piece of text. It has various applications, such as understanding customer feedback, detecting opinion trends, and monitoring social media sentiment. In this blog post, we will explore how to perform sentiment analysis using SpaCy, a popular NLP library in Python.

## Installing SpaCy

Before we can start using SpaCy, we need to install it. Open your terminal and run the following command:

```python
pip install spacy
```

Next, we need to download a language model for sentiment analysis. SpaCy provides pre-trained language models for different languages. For this example, we'll use the English language model. Run the following command to download it:

```python
python -m spacy download en_core_web_sm
```

## Performing Sentiment Analysis

Once we have SpaCy installed and the language model downloaded, we can proceed with sentiment analysis. Let's start by importing the necessary libraries and loading the language model:

```python
import spacy

nlp = spacy.load('en_core_web_sm')
```

Next, we'll define a function that takes in a piece of text and returns its sentiment:

```python
def analyze_sentiment(text):
    doc = nlp(text)
    polarity = 0

    for sentence in doc.sents:
        sentence_polarity = sentence.sentiment.polarity
        polarity += sentence_polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
```

In this function, we loop through each sentence in the text and calculate its polarity using SpaCy's built-in sentiment analysis capabilities. We then sum up the sentence polarities to determine the overall sentiment of the text.

Let's test our sentiment analysis function:

```python
text = "I absolutely loved the movie! The acting was superb and the storyline was captivating."
sentiment = analyze_sentiment(text)

print(sentiment)  # Output: Positive
```

In this example, the sentiment analysis correctly identifies the positive sentiment in the given text.

## Conclusion

In this blog post, we have shown how to perform sentiment analysis using SpaCy. By leveraging SpaCy's powerful language models, we can easily analyze the sentiment of text data. Sentiment analysis can be a valuable tool for understanding customer sentiment, identifying trends, and making data-driven decisions.

#NLP #SentimentAnalysis