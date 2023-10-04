---
layout: post
title: "Convolutional Neural Network를 사용한 파이썬 Sentiment analysis 알고리즘 개발"
description: " "
date: 2023-10-04
tags: [DeepLearning, SentimentAnalysis]
comments: true
share: true
---

## 서론
감성 분석은 텍스트 데이터에서 사용자의 감정이나 태도를 파악하는 중요한 작업입니다. 최근에는 Convolutional Neural Network (CNN)을 이용한 감성 분석 알고리즘의 성능이 뛰어나다는 것이 입증되었습니다. 본 문서에서는 파이썬을 사용하여 CNN을 활용한 감성 분석 알고리즘을 개발하는 방법을 다루겠습니다.

## CNN이란?
Convolutional Neural Network (CNN)은 주로 이미지 처리 작업에서 사용되는 딥러닝 알고리즘입니다. 그러나 CNN은 텍스트 데이터에도 효과적으로 적용될 수 있습니다. 텍스트 데이터를 시각화된 형태로 변환하고, 이를 기반으로 패턴을 학습하여 분석 결과를 도출할 수 있습니다.

## 데이터 준비
CNN을 사용한 감성 분석 알고리즘을 개발하기 위해서는 적절한 학습 데이터가 필요합니다. 이 예제에서는 감정 라벨링된 영화 리뷰 데이터를 사용하겠습니다. 학습 데이터와 테스트 데이터를 준비하여 저장합니다.

```python
import pandas as pd

# 학습 데이터 로드
train_data = pd.read_csv('train_data.csv')

# 테스트 데이터 로드
test_data = pd.read_csv('test_data.csv')
```

## 텍스트 전처리
텍스트 데이터는 다양한 형태로 구성되어 있기 때문에 통일된 형태로 전처리 과정이 필요합니다. 주요한 전처리 과정으로는 토큰화(Tokenization), 불용어 제거(Stopword Removal), 단어 임베딩(Word Embedding) 등이 있습니다.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 불용어 제거
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 소문자 변환
    text = text.lower()
    
    # 토큰화
    tokens = word_tokenize(text)
    
    # 불용어 제거
    tokens = [token for token in tokens if token not in stop_words]
    
    return tokens

# 텍스트 전처리
train_data['text'] = train_data['text'].apply(preprocess_text)
test_data['text'] = test_data['text'].apply(preprocess_text)

# 단어 임베딩
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data['text'])
train_sequences = tokenizer.texts_to_sequences(train_data['text'])
test_sequences = tokenizer.texts_to_sequences(test_data['text'])

# 시퀀스 패딩
max_len = 100
train_sequences = pad_sequences(train_sequences, maxlen=max_len)
test_sequences = pad_sequences(test_sequences, maxlen=max_len)
```

## 모델 구성
CNN을 사용한 감성 분석을 위해 필요한 모델을 구성합니다. 텍스트 데이터의 시퀀스를 입력으로 받아서 감성을 분석하는 모델을 구성할 수 있습니다.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense

vocab_size = len(tokenizer.word_index) + 1

model = Sequential()
model.add(Embedding(vocab_size, 128, input_length=max_len))
model.add(Conv1D(256, 5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()
```

## 모델 학습
구성한 모델을 학습 데이터에 대해 학습시킵니다.

```python
history = model.fit(train_sequences, train_data['label'], epochs=10, batch_size=64, validation_split=0.2)
```

## 모델 평가
학습이 완료된 모델을 테스트 데이터에 대해 평가합니다.

```python
loss, accuracy = model.evaluate(test_sequences, test_data['label'])
print('Test Accuracy:', accuracy)
```

## 결론
본 문서에서는 파이썬을 사용하여 Convolutional Neural Network (CNN)을 활용한 감성 분석 알고리즘을 개발하는 방법을 소개하였습니다. CNN은 텍스트 데이터에서의 감성 분석에도 유용하게 적용될 수 있으며, 알맞은 데이터 전처리와 모델 구성을 통해 정확한 결과를 얻을 수 있습니다.

#DeepLearning #SentimentAnalysis