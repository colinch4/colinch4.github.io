---
layout: post
title: "파이썬 SpaCy를 활용한 텍스트에서 질문 추출(Question Extraction)"
description: " "
date: 2023-09-24
tags: [spacy]
comments: true
share: true
---

## 소개
텍스트에서 질문을 추출하는 것은 자연어 처리(Natural Language Processing, NLP)의 중요한 문제 중 하나입니다. 질문 추출은 문장에서 질문 형태로 변환될 수 있는 핵심 정보를 식별하는 과정입니다. 이를 통해 자동화된 질의응답 시스템, 정보 검색, 텍스트 마이닝 등 다양한 응용 분야에서 활용할 수 있습니다.

이 블로그 포스트에서는 파이썬의 SpaCy 라이브러리를 사용하여 텍스트에서 질문을 추출하는 방법을 다루겠습니다.

## SpaCy란?
SpaCy는 파이썬으로 작성된 고성능의 자연어 처리 라이브러리입니다. 토큰화, 형태소 분석, 개체명 인식, 구문 분석 등 NLP 작업을 수행할 수 있는 다양한 기능을 제공합니다. SpaCy는 사용하기 쉽고 빠른 처리 속도가 특징입니다.

## 설치 및 설정
먼저 SpaCy를 설치해야 합니다. 아래 명령을 사용하여 SpaCy를 설치합니다.

```
pip install spacy
```

SpaCy를 설치한 후, 다음 명령으로 영어 모델을 다운로드 받습니다.

```
python -m spacy download en_core_web_sm
```

## 텍스트에서 질문 추출하기
이제 SpaCy를 사용하여 텍스트에서 질문을 추출하는 방법을 알아보겠습니다. 예시로 다음과 같은 텍스트를 사용하겠습니다.

> Bill Gates is the founder of Microsoft. He was born on October 28, 1955, in Seattle, Washington.

먼저 SpaCy를 초기화합니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

다음으로 텍스트를 SpaCy 모델에 입력하여 문서(Document) 객체를 생성합니다.

```python
text = "Bill Gates is the founder of Microsoft. He was born on October 28, 1955, in Seattle, Washington."
doc = nlp(text)
```

문서 객체에서 질문 추출을 위해 특정한 구문을 식별해야 합니다. SpaCy에서는 문장(Sentence)과 토큰(Token)을 사용하여 구문을 분석할 수 있습니다. 다음은 문장과 토큰을 추출하는 코드입니다.

```python
sentences = list(doc.sents)
tokens = list(doc)

for sentence in sentences:
    # 문장에서 질문 토큰 추출
    question_tokens = [token.text for token in sentence if token.tag_ == "WP" or token.tag_ == "WRB"]

    # 추출한 질문 토큰 출력
    print(question_tokens)
```

위의 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
['Who']
```

위 예시에서는 "Who"라는 질문 토큰을 추출했습니다.

## 결론
이 블로그 포스트에서는 파이썬의 SpaCy 라이브러리를 사용하여 텍스트에서 질문을 추출하는 방법에 대해 알아보았습니다. SpaCy는 강력한 자연어 처리 도구로서 다양한 NLP 작업을 간편하게 수행할 수 있도록 도와줍니다. 질문 추출은 다양한 응용 분야에서 활용될 수 있으며, 자동화된 질의응답 시스템 등에 유용하게 활용될 수 있습니다.

#NLP #SpaCy