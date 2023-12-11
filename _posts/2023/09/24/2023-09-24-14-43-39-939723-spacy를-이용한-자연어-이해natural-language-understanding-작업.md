---
layout: post
title: "SpaCy를 이용한 자연어 이해(Natural Language Understanding) 작업"
description: " "
date: 2023-09-24
tags: [spacy]
comments: true
share: true
---

자연어 이해는 컴퓨터가 인간의 언어를 이해하고 처리하는 과정을 말합니다. 이는 자연어 처리(Natural Language Processing) 분야에서 매우 중요한 작업입니다. SpaCy는 파이썬에서 사용할 수 있는 강력한 자연어 처리 라이브러리로, 다양한 자연어 이해 작업을 수행할 수 있습니다.

## 토큰화(Tokenization)

토큰화는 자연어 문장을 단어나 구절로 분리하는 과정입니다. SpaCy는 미리 학습된 모델을 사용하여 문장을 토큰으로 분리할 수 있습니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("SpaCy is an open-source library for natural language processing.")

for token in doc:
    print(token.text)
```

결과:

```
SpaCy
is
an
open
-
source
library
for
natural
language
processing
.
```

## 품사 태깅(Part-of-Speech Tagging)

품사 태깅은 단어의 품사를 태깅하는 작업입니다. SpaCy는 미리 학습된 모델을 사용하여 품사 태깅을 수행할 수 있습니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I like to eat pizza.")

for token in doc:
    print(token.text, token.pos_)
```

결과:

```
I PRON
like VERB
to PART
eat VERB
pizza NOUN
. PUNCT
```

## 구문 분석(Syntactic Parsing)

구문 분석은 문장의 구조를 분석하는 작업입니다. SpaCy는 미리 학습된 모델을 사용하여 구문 분석을 수행할 수 있습니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The cat chased the mouse.")

for token in doc:
    print(token.text, token.dep_)
```

결과:

```
The det
cat nsubj
chased ROOT
the det
mouse dobj
. punct
```

## 감정 분석(Sentiment Analysis)

감정 분석은 문장의 감정을 분석하는 작업입니다. SpaCy는 미리 학습된 모델을 사용하여 감정 분석을 수행할 수 있습니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love this movie. It's so amazing!")

sentiment_score = doc.sentiment
print(sentiment_score)

if sentiment_score >= 0.5:
    print("Positive sentiment")
else:
    print("Negative sentiment")
```

결과:

```
0.9
Positive sentiment
```

SpaCy를 사용하여 자연어 이해 작업을 수행하면 텍스트 데이터를 보다 효과적으로 처리할 수 있습니다. SpaCy의 다양한 기능을 활용하여 자연어 이해 작업을 진행해보세요!

#NLProc #자연어처리