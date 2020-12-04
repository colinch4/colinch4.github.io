---
layout: post
title: "[머신러닝] Logistic Regression 0"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# Logistic Regression 기초

> Linear Regression과 별개로 Logistic Regression은 연속적인 값을 추록하는것이 아니라 **Classification**하는 하나의 방법이다. 



## classification (분류)

> classification은 Training DataSet 특성과 분포를 파악한 후 미지의 입력 데이터에 대해 어떠한 종류의 값으로 분류될 수 있는지 예측하는 모델이다.

* 정확도 측정이 가능하다.

* Binary classification : 2개중 1개로 분류한다.

  통상적으로 0.5이상이면 1로 Pass, 0.5미만이면 0으로 Fail로 예측된다.

* Multinomial classification: m개중 1개로 분류한다.

* 예를 들면, 

  E-mail 스팸 여부 예측, MRI 사진 분석 후 악성/일반 종양 여부, 신용카드 도난 카드 여부 등이 있다.

* 알고리즘으로는 SVM, Naive Bayse, Logistic Regression 등이 있다.



## Logistic Regression

> Logistic Regression은 classification 방법 중 하나로 정확도가 상당히 높고 Deep Learning의 기본모델이다.

![image-20201005014945703](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005014945703.png?raw=true)

* Q. Linear Regression으로 Classification 하도록 학습과 예측을 할 수 있지 않을까?

​        A. 직선이기 때문에 1이상의 값이 도출하는 등의 문제가 발생한다. 

![image-20201005022930513](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005022930513.png?raw=true)



## Sigmoid 함수

> 위의 문제점 때문에 Sigmoid 함수를 도입한다.

![image-20201005183401720](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005183401720.png?raw=true)

![image-20201005023426783](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005023426783.png?raw=true)

## 회귀 모델(Hypothesis, predictive Model)

> Logistic Regression의 회귀 함수를 정의한다.

![image-20201005183431592](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005183431592.png?raw=true)



## Cross Entropy

> Linear Regression에서 사용하던 Loss function을 사용하면 Loss의 convex 성질이 사라지게 된다. 따라서 Cross Entropy를 사용하게 된다.

![image-20201005183501246](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005183501246.png?raw=true)