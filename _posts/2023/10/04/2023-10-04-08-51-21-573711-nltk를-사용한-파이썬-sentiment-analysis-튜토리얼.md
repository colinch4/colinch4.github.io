---
layout: post
title: "NLTK를 사용한 파이썬 Sentiment analysis 튜토리얼"
description: " "
date: 2023-10-04
tags: [NLTK, SentimentAnalysis]
comments: true
share: true
---

Sentiment analysis는 텍스트 데이터의 감성(positive, negative, neutral)을 분석하는 기술입니다. 이 튜토리얼에서는 파이썬의 Natural Language Toolkit (NLTK)를 사용하여 Sentiment analysis를 수행하는 방법을 알아보겠습니다.

## NLTK 설치

NLTK를 사용하기 위해 먼저 NLTK 라이브러리를 설치해야 합니다. 다음 명령어를 사용하여 NLTK를 설치합니다:

```python
pip install nltk
```

## 데이터셋 준비

Sentiment analysis를 수행하기 위해 사용할 데이터셋을 준비해야 합니다. 이 튜토리얼에서는 영화 리뷰 데이터셋을 사용할 예정입니다. "nltk.corpus" 모듈을 사용하여 데이터셋을 불러오겠습니다.

```python
import nltk

nltk.download('movie_reviews')
```

## 데이터 전처리

데이터를 불러온 후에는 전처리 과정을 통해 텍스트 데이터를 정제해야 합니다. 이 단계에서는 다음과 같은 작업을 수행합니다:

1. 토큰화(Tokenization): 텍스트를 단어 단위로 나누는 작업을 수행합니다.
2. 불용어 제거(Stopword removal): 영어에서 의미 없는 단어를 제거합니다.
3. 단어 정규화(Stemming or Lemmatization): 단어를 기본 형태로 변환합니다.

```python
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    # 토큰화
    tokens = word_tokenize(text)
    
    # 불용어 제거
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # 단어 정규화
    stemmer = PorterStemmer()
    normalized_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    return normalized_tokens

```

## 피처 추출

전처리된 데이터를 기반으로 피처를 추출하는 단계입니다. 이 튜토리얼에서는 간단한 방법으로 BOW(Bag of Words) 피처를 추출하겠습니다.

```python
from sklearn.feature_extraction.text import CountVectorizer

def extract_features(texts):
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(texts)
    
    return features.toarray()

```

## 모델 학습 및 평가

데이터셋을 학습 데이터와 테스트 데이터로 나눈 후에는 ML 모델을 학습하고 평가해야 합니다. 이 튜토리얼에서는 Logistic Regression 모델을 사용하여 Sentiment analysis를 수행하겠습니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 데이터셋 준비
positive_reviews = [preprocess_text(movie_reviews.raw(fileid)) for fileid in movie_reviews.fileids(categories=['pos'])]
negative_reviews = [preprocess_text(movie_reviews.raw(fileid)) for fileid in movie_reviews.fileids(categories=['neg'])]
labels = ['positive'] * len(positive_reviews) + ['negative'] * len(negative_reviews)
reviews = positive_reviews + negative_reviews

# 피처 추출
features = extract_features(reviews)

# 학습 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 테스트 데이터 평가
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

```

## 결론

이 튜토리얼에서는 NLTK를 사용하여 파이썬에서 Sentiment analysis를 수행하는 방법을 알아보았습니다. Sentiment analysis를 통해 텍스트 데이터의 감성을 분석할 수 있으며, 이를 활용하여 감성 분석 기반의 다양한 응용 프로그램을 개발할 수 있습니다. NLTK 라이브러리는 텍스트 마이닝 작업을 수행하는 데 매우 유용한 도구입니다. 추가적인 자세한 내용은 NLTK 공식 문서를 참고하시기 바랍니다. 

Happy coding! :smiley: #NLTK #SentimentAnalysis