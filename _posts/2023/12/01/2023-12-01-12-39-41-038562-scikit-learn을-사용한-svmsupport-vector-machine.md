---
layout: post
title: "[python] scikit-learn을 사용한 SVM(Support Vector Machine)"
description: " "
date: 2023-12-01
tags: [python]
comments: true
share: true
---

Support Vector Machine (SVM)은 지도학습 알고리즘 중 하나로, 데이터 분류와 회귀 문제에 사용됩니다. SVM은 분류를 위해 결정 경계를 찾는 기계 학습 방법입니다.

scikit-learn은 파이썬을 위한 머신러닝 라이브러리로, SVM을 구현하기 위한 다양한 기능을 제공합니다. 이번 포스트에서는 scikit-learn을 사용하여 SVM을 실행하는 방법을 살펴보겠습니다.

## 필요한 라이브러리 설치하기

scikit-learn을 설치하기 위해서는 파이썬 패키지 관리자인 `pip`를 사용할 수 있습니다. 아래의 명령어를 사용하여 설치해주세요:

```python
pip install -U scikit-learn
```

## 데이터 로드하기

SVM을 실행하기 위해서는 분류하고자 하는 데이터가 필요합니다. 예를 들어, iris 데이터셋을 사용해보겠습니다:

```python
from sklearn.datasets import load_iris

# iris 데이터셋 로드하기
iris = load_iris()

# 데이터의 특성과 클래스 확인하기
print(iris.data)
print(iris.target)
```

## 모델 학습하기

scikit-learn의 SVM 모델을 사용하여 학습을 진행할 수 있습니다. 다음은 iris 데이터셋을 사용하여 SVM 모델을 학습하는 예제입니다:

```python
from sklearn import svm

# SVM 모델 생성하기
model = svm.SVC()

# 데이터를 학습시키기
model.fit(iris.data, iris.target)
```

## 예측하기

학습된 모델을 사용하여 새로운 데이터에 대한 예측을 할 수 있습니다:

```python
# 새로운 데이터 생성하기
new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.9, 4.3, 1.3]]

# 예측하기
predictions = model.predict(new_data)
print(predictions)
```

## 결과 확인하기

예측 결과를 확인하기 위해 예측한 클래스 레이블을 실제 클래스 레이블과 비교할 수 있습니다:

```python
# 실제 클래스 레이블 확인하기
true_labels = ["setosa", "versicolor", "virginica"]

# 예측한 클래스 레이블과 실제 클래스 레이블 비교하기
for i, prediction in enumerate(predictions):
    print("Predicted: {} / Actual: {}".format(true_labels[prediction], true_labels[iris.target[i]]))
```

## 결론

scikit-learn을 사용하여 SVM 모델을 구현하고 데이터를 분류하는 방법을 살펴보았습니다. SVM은 강력한 분류기로 알려져 있으며, scikit-learn의 다른 기능과 함께 사용하면 좀 더 복잡한 머신러닝 문제를 해결할 수 있습니다.

참고 자료:
- scikit-learn 공식 문서: [https://scikit-learn.org/stable/modules/svm.html](https://scikit-learn.org/stable/modules/svm.html)