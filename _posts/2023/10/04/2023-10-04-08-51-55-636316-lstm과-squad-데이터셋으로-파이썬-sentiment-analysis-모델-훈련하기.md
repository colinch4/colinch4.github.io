---
layout: post
title: "LSTM과 Squad 데이터셋으로 파이썬 Sentiment analysis 모델 훈련하기"
description: " "
date: 2023-10-04
tags: [python]
comments: true
share: true
---

이번 블로그 포스트에서는 Long Short-Term Memory (LSTM) 알고리즘과 Squad 데이터셋을 사용하여 파이썬으로 Sentiment Analysis 모델을 훈련하는 방법을 알아보겠습니다. Sentiment Analysis는 문장이나 문서의 감성을 예측하는 자연어 처리(Natural Language Processing, NLP) 작업입니다. LSTM은 순환 신경망(RNN)의 한 종류로, 시계열 데이터를 처리하고 기존의 메모리 유닛의 단점을 보완하는데 사용됩니다.

## 1. 데이터셋 소개

이번 예제에서는 Squad 데이터셋을 사용합니다. Squad(Span-Question Answering Dataset)는 질문과 그에 대한 답변이 있는 문서로 구성된 데이터셋으로, 문장의 감성을 예측하는데 활용할 수 있습니다. Squad 데이터셋은 [공식 사이트](https://rajpurkar.github.io/SQuAD-explorer/)에서 다운로드할 수 있습니다.

## 2. 데이터 전처리

데이터를 사용하기 전에 전처리 과정이 필요합니다. 데이터를 로드한 다음 문장과 감성(label)으로 분리합니다. 문장은 토큰화(tokenization)하여 형태소 분석을 수행합니다. 문장 토큰화는 `nltk` 라이브러리의 `word_tokenize` 함수를 사용하여 수행할 수 있습니다.

```python
import nltk

# 데이터 로드
data = load_data()

sentences = []
labels = []

for item in data:
    sentence = item['context']
    label = item['label']
    
    # 문장 토큰화
    tokens = nltk.word_tokenize(sentence)
    
    sentences.append(tokens)
    labels.append(label)
```

## 3. LSTM 모델 훈련

전처리된 데이터를 사용하여 LSTM 모델을 훈련합니다. 각 토큰을 임베딩(embedding)하여 순환 신경망에 입력으로 제공합니다. LSTM 층은 `keras` 라이브러리의 `LSTM` 클래스를 사용하여 추가할 수 있습니다.

```python
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding

# 임베딩 크기
embedding_dim = 100

# LSTM 모델 생성
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim))
model.add(LSTM(units=100))
model.add(Dense(units=1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit(np.asarray(sentences), np.asarray(labels), batch_size=32, epochs=10)
```

## 4. 모델 평가

훈련된 모델을 사용하여 감성 분석을 수행하고 평가합니다. 테스트 데이터를 사용하여 예측 결과를 확인합니다.

```python
# 테스트 데이터 로드
test_data = load_test_data()

test_sentences = []
test_labels = []

for item in test_data:
    sentence = item['context']
    label = item['label']
    
    # 문장 토큰화
    tokens = nltk.word_tokenize(sentence)
    
    test_sentences.append(tokens)
    test_labels.append(label)

# 감성 예측
predictions = model.predict(np.asarray(test_sentences))

# 평가
accuracy = np.mean(predictions == test_labels)
```

## 마무리

이번 블로그 포스트에서는 LSTM 알고리즘과 Squad 데이터셋을 사용하여 파이썬으로 Sentiment Analysis 모델을 훈련하는 방법을 알아보았습니다. LSTM은 순환 신경망의 특징을 이용하여 시계열 데이터를 처리하고 감성 분석과 같은 자연어 처리 작업에 활용됩니다. Squad 데이터셋을 사용하여 모델을 훈련하고 평가하는 과정을 진행했습니다.

더 자세한 내용은 [공식 문서](https://keras.io/api/layers/recurrent_layers/lstm/)와 [Squad 데이터셋 사이트](https://rajpurkar.github.io/SQuAD-explorer/)를 참고하세요.

#AI #SentimentAnalysis