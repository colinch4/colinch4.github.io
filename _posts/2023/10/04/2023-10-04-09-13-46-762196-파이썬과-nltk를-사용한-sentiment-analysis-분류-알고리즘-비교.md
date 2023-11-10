---
layout: post
title: "파이썬과 NLTK를 사용한 Sentiment analysis 분류 알고리즘 비교"
description: " "
date: 2023-10-04
tags: [파이썬]
comments: true
share: true
---

Sentiment Analysis, 또는 감성 분석은 자연어 처리 기술을 통해 텍스트의 긍정적인, 부정적인 또는 중립적인 감정을 분류하는 기술입니다. 이러한 기술은 소셜 미디어, 제품 리뷰, 기사 등 다양한 텍스트 데이터에서 감정 및 의견을 추출하는 데 사용됩니다.

파이썬은 다양한 자연어 처리 라이브러리를 제공하며, NLTK(Natural Language Toolkit)는 그 중 하나로 가장 널리 사용되는 라이브러리입니다. NLTK는 토큰화, 형태소 분석, 문장 분리, 감성 분석 등 다양한 자연어 처리 기능을 제공합니다. 이번 글에서는 NLTK를 사용하여 Sentiment Analysis를 수행할 때 사용되는 여러 알고리즘들을 비교해보겠습니다. 

## 알고리즘 비교

### 1. Naive Bayes Classifier

Naive Bayes 분류기는 베이즈 정리를 기반으로 하며, 단어의 확률 분포를 사용하여 감성 분류를 수행합니다. 이 알고리즘은 간단하고 효율적이지만, 단어의 독립성 가정을 하는 것이 주요한 단점입니다.

```python
from nltk.classify import NaiveBayesClassifier

# 학습 데이터 준비
train_data = [("I love this movie", "positive"),
              ("This movie is terrible", "negative"),
              ("The acting was excellent", "positive")]

# 피처 추출 함수 정의
def extract_features(text):
    words = text.lower().split()
    return dict([(word, True) for word in words])

# 학습 데이터로 분류기 학습
featureset = [(extract_features(text), sentiment) for (text, sentiment) in train_data]
classifier = NaiveBayesClassifier.train(featureset)

# 분류기로 예측 수행
text = "This movie is amazing"
predicted_sentiment = classifier.classify(extract_features(text))
print(predicted_sentiment)  # 출력: "positive"
```

### 2. Decision Tree Classifier

Decision Tree 분류기는 트리 형태의 결정 규칙을 기반으로 하며, 텍스트 데이터에서 특징을 추출하여 분류를 수행합니다. 이 알고리즘은 해석하기 쉽고 설명력이 높지만, 과적합될 수 있는 가능성이 있습니다.

```python
from nltk.classify import DecisionTreeClassifier

# 학습 데이터 준비
train_data = [("I love this movie", "positive"),
              ("This movie is terrible", "negative"),
              ("The acting was excellent", "positive")]

# 피처 추출 함수 정의
def extract_features(text):
    words = text.lower().split()
    return dict([(word, True) for word in words])

# 학습 데이터로 분류기 학습
featureset = [(extract_features(text), sentiment) for (text, sentiment) in train_data]
classifier = DecisionTreeClassifier.train(featureset)

# 분류기로 예측 수행
text = "This movie is amazing"
predicted_sentiment = classifier.classify(extract_features(text))
print(predicted_sentiment)  # 출력: "positive"
```

### 3. Support Vector Machine (SVM) Classifier

SVM 분류기는 텍스트 분류 작업에 좋은 성능을 보이는 알고리즘입니다. SVM은 텍스트 데이터를 벡터로 변환하여 감성 분류를 수행합니다. 이 알고리즘은 복잡한 문제에 대해서도 잘 작동하지만, 학습과 예측에 시간과 메모리가 많이 소요될 수 있습니다.

```python
from nltk.classify import SklearnClassifier
from sklearn.svm import SVC

# 학습 데이터 준비
train_data = [("I love this movie", "positive"),
              ("This movie is terrible", "negative"),
              ("The acting was excellent", "positive")]

# 피처 추출 함수 정의
def extract_features(text):
    words = text.lower().split()
    return dict([(word, True) for word in words])

# 학습 데이터로 분류기 학습
featureset = [(extract_features(text), sentiment) for (text, sentiment) in train_data]
classifier = SklearnClassifier(SVC()).train(featureset)

# 분류기로 예측 수행
text = "This movie is amazing"
predicted_sentiment = classifier.classify(extract_features(text))
print(predicted_sentiment)  # 출력: "positive"
```

## 결론

이번 글에서는 파이썬과 NLTK를 사용하여 Sentiment Analysis를 수행할 때 사용되는 여러 알고리즘들을 비교해보았습니다. 각각의 알고리즘은 각자의 장단점이 있으며, 데이터셋의 특성에 따라 성능이 달라질 수 있습니다. 따라서 적절한 알고리즘을 선택하는 것이 중요합니다.