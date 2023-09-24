---
layout: post
title: "Text summarization in NLP using Python"
description: " "
date: 2023-09-24
tags: [TextSummarization]
comments: true
share: true
---
In the field of Natural Language Processing (NLP), text summarization plays a vital role in extracting the most important information from a text document. It saves time and effort by condensing lengthy articles or documents into shorter versions while preserving the key ideas and main points. In this blog post, we will explore a Python library called `gensim` to perform text summarization using the TextRank algorithm.

## Introduction to TextRank Algorithm
TextRank is an unsupervised algorithm inspired by Google's PageRank algorithm. It views a text document as a graph representation, where sentences act as nodes, and the relationships between sentences are represented by edges. By calculating the relevance and importance of each sentence, TextRank identifies the most significant sentences as the summary.

## Installing Gensim
Before we dive into implementing text summarization, let's install the `gensim` library. Open your terminal or command prompt and execute the following command:

```python
pip install gensim
```

## Implementing Text Summarization with Gensim
Now, let's write a Python script to perform text summarization using the TextRank algorithm with `gensim`.

```python
import gensim
from gensim.summarization import summarize

# Define the text document
text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nullam mattis tristique bibendum. Vestibulum vulputate orci nisi, vitae 
bibendum eros sollicitudin at. Sed at eleifend magna, sit amet fringilla
diam. Mauris posuere nisl vel diam scelerisque, eget vehicula massa posuere. 
Morbi ultricies neque non facilisis tempus. Cras malesuada arcu id urna 
dapibus, sit amet pretium sem interdum. Donec id quam vitae enim viverra 
lacinia nec vitae eros.

Duis condimentum, justo non feugiat bibendum, arcu sapien rutrum nisl, 
ac interdum nibh eros in mi. Vivamus bibendum justo ac posuere interdum. 
Praesent feugiat lorem enim, vitae elementum eros sollicitudin nec. Cras 
nec sollicitudin ligula, in viverra est. Duis maximus quam eget euismod
fringilla. Nulla facilisi. Quisque semper bibendum diam non pretium.

Phasellus et tristique nibh. Mauris quis eleifend metus. Ut tincidunt 
condimentum mauris vel vestibulum. Etiam magna felis, aliquet vitae 
lectus eu, sagittis aliquam justo. Nunc nec viverra dui, sit amet commodo 
neque. Nam bibendum, magna at efficitur iaculis, turpis enim efficitur 
ex, ut facilisis odio mi ac arcu.

'''

# Set the summary ratio
summary_ratio = 0.2

# Generate the summary
summary = summarize(text, ratio=summary_ratio)

# Print the summary
print(summary)
```

## Usage and Output
In the script, we define a text document to summarize and set the summary ratio to 0.2, indicating that we want to generate a summary that is 20% of the original text length. The `summarize` function from `gensim` takes care of the rest, returning the summarized text.

When you run the script, the output will be the summary of the given text document. Feel free to adjust the summary ratio to experiment with different summary lengths.

## Conclusion
Text summarization using Python and the TextRank algorithm enables us to quickly extract important information from lengthy documents or articles. By leveraging the `gensim` library, we can easily incorporate text summarization capabilities into our NLP projects. So go ahead, try it out, and see how it can benefit your text analysis tasks!

#NLP #TextSummarization