---
layout: post
title: "SpaCy를 이용하여 텍스트에서 부정적인 감정 단어 추출(Negative Word Extraction)"
description: " "
date: 2023-09-24
tags: [spacy]
comments: true
share: true
---

부정적인 감정 단어들을 텍스트 데이터에서 추출하는 것은 감정 분석, 감성 분석 등의 자연어 처리 작업에서 중요한 과제입니다. 이번 포스트에서는 SpaCy 라이브러리를 사용하여 텍스트에서 부정적인 감정 단어를 추출하는 방법에 대해 알아보겠습니다.

## SpaCy 소개

SpaCy는 파이썬에서 사용할 수 있는 고성능 자연어 처리 라이브러리입니다. SpaCy는 토큰화, 형태소 분석, 개체명 인식 등 다양한 자연어 처리 작업을 처리할 수 있으며, 일반적으로 NLTK(Natural Language Toolkit)와 비교하여 높은 처리 속도와 효율성을 제공합니다.

## 부정적인 감정 단어 추출하기

1. SpaCy 설치하기

먼저, SpaCy를 설치해야 합니다. 아래의 명령을 사용하여 SpaCy를 설치할 수 있습니다.

```shell
pip install spacy
```

2. 언어 모델 설치하기

SpaCy는 언어별로 모델을 제공합니다. 텍스트에서 부정적인 감정 단어를 추출하기 위해서는 해당 언어의 모델을 설치해야 합니다. 예를 들어, 영어 모델을 설치하려면 아래의 명령을 사용합니다.

```shell
python -m spacy download en_core_web_sm
```

3. 텍스트에서 부정적인 감정 단어 추출하기

SpaCy를 사용하여 텍스트에서 부정적인 감정 단어를 추출하는 예제 코드를 작성해보겠습니다.

```python
import spacy

# 언어 모델 불러오기
nlp = spacy.load("en_core_web_sm")

# 텍스트 문장
text = "I am really disappointed with the customer service."

# 문장을 처리하여 토큰화
doc = nlp(text)

# 부정적인 감정 단어 추출
negative_words = []
for token in doc:
    if token.is_alpha and token.sentiment < 0:
        negative_words.append(token.text)

# 추출된 부정적인 감정 단어 출력
print(negative_words)
```

위의 코드에서는 SpaCy를 사용하여 영어 모델을 불러오고, 텍스트 문장을 토큰화하여 부정적인 감정 단어를 추출하였습니다. 추출된 부정적인 감정 단어는 리스트에 저장되어 출력됩니다.

## 마무리

이번 포스트에서는 SpaCy를 사용하여 텍스트에서 부정적인 감정 단어를 추출하는 방법에 대해 알아보았습니다. SpaCy를 활용하여 자연어 처리 작업을 보다 쉽게 수행할 수 있으며, 이를 활용하여 감정 분석, 감성 분석 등 다양한 자연어 처리 작업을 수행할 수 있습니다. #SpaCy #NegativeWordExtraction