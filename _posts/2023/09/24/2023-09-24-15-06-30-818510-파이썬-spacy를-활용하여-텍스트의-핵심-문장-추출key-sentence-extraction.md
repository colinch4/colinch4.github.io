---
layout: post
title: "파이썬 SpaCy를 활용하여 텍스트의 핵심 문장 추출(Key Sentence Extraction)"
description: " "
date: 2023-09-24
tags: [SpaCy]
comments: true
share: true
---

텍스트 데이터에서 핵심 문장을 추출하는 것은 텍스트 요약, 문서 분류, 자동 문서 요약 등 다양한 자연어 처리(Natural Language Processing, NLP) 작업에 유용합니다. 이번 포스트에서는 파이썬의 SpaCy 라이브러리를 사용하여 텍스트의 핵심 문장을 추출하는 방법에 대해 알아보겠습니다.

## SpaCy 라이브러리 설치

먼저, SpaCy 라이브러리를 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```
pip install spacy
```

## 모델 다운로드

SpaCy는 자체적으로 학습된 언어 모델을 제공합니다. 이 모델을 다운로드하여 사용할 수 있습니다. 예를 들어, 영어에 대한 모델은 다음과 같이 다운로드할 수 있습니다.

```
python -m spacy download en_core_web_sm
```

## 텍스트의 핵심 문장 추출

아래는 SpaCy를 사용하여 텍스트에서 핵심 문장을 추출하는 예제 코드입니다. 이 코드는 다음과 같은 단계로 작동합니다.

1. SpaCy 라이브러리를 불러옵니다.
2. 언어 모델을 로드합니다.
3. 텍스트를 처리하여 문장을 추출합니다.
4. 각 문장의 중요도를 계산합니다.
5. 가장 중요한 문장을 반환합니다.

```python
import spacy

def extract_key_sentences(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    sentences = [sent.text for sent in doc.sents]
    sentence_scores = {}

    for sent in doc.sents:
        for token in sent:
            if token.text.lower() in sentence_scores:
                sentence_scores[token.text.lower()] += token.rank
            else:
                sentence_scores[token.text.lower()] = token.rank

    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    key_sentences = []
    for sentence, score in sorted_sentences[:3]:
        key_sentences.append(sentence)

    return key_sentences

text = "SpaCy is an open-source library for advanced Natural Language Processing in Python. It provides efficient pipelines for text processing and nlp tasks such as part-of-speech tagging, named entity recognition, dependency parsing, and sentence segmentation. With SpaCy, we can easily extract key sentences from text data."

key_sentences = extract_key_sentences(text)
for idx, sentence in enumerate(key_sentences):
    print(f"Key sentence {idx+1}: {sentence}")
```

위의 코드를 실행하면 주어진 텍스트에서 가장 핵심적인 문장이 3개 추출됩니다. 이를 활용하여 요약이나 분석 등 다양한 작업에 활용할 수 있습니다.

## 마무리

이번 포스트에서는 파이썬의 SpaCy 라이브러리를 사용하여 텍스트의 핵심 문장을 추출하는 방법에 대해 알아보았습니다. SpaCy는 다양한 자연어 처리 작업을 지원하며, 간편하고 효율적인 텍스트 처리를 제공합니다. 텍스트 요약, 문서 분류, 자동 문서 생성 등의 작업을 위해 SpaCy를 활용해 보세요.

#NLP #SpaCy