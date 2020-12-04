---
layout: post
title: "성능평가 지표(Evaluation Metrics)"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# 성능평가 지표(Evaluation Metrics)

> 기계학습에서 모델의 분류 성능 평가에 사용되는 지표에 대해서 언급한다.
>
> 어느 모델이든 발전을 위한 feedback은 현재 모델의 performance을 올바르게 평하는 것부터 시작한다.



## 모델의 분류와 정답

> 모델을 평가하는 요소에 있어서 모델이 내놓은 정답과 실제 정답의 관계로 부터 정의 한다.



<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/confusion_matrix.png" alt="confusion_matrix" style="zoom:80%;" />

여기서 True는 정답을 맞춘것을 의미하고 Positive, Negative는 분류결과가 True, False인지를 의미한다.

* True Positive(TP) : 정답을 True 라고 해서 맞음     (정답)

* False Positive(FP) : 정답을 True 라고 해서 틀림    (오답)

* False Negative(FN) : 정답을 False라고 해서 틀림  (오답)

* True Negative(TN) : 정답을 False라고 해서 맞음   (정답)



## 자주 사용하는 평가 지표들

> Precision, Recall, Accuracy, F1-Score 등에 대해서 알아본다.
>
> ~~(나중에 더 알게되는 지표가 있다면 추가 할 예정)~~



#### 1. Precision(정밀도)

> Positive Predictive Value(PPV)라고도 불린다.
>
>  **True 라고 예측**( → Positive )해서 정답( → True)인 비율, 


![image-20201123161700506](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201123161700506.png?raw=true)



#### 2. Recall(재현율)

> Sensitivity 또는 hit rate 라고도 불린다.
>
> **정답이 True** 인것중에 모델이 True 라고 예측한 비율

![image-20201123204544691](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201123204544691.png?raw=true)

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/confusion_matrix1.png" alt="confusion_matrix1" style="zoom: 67%;" />


#### (벤다이어그램)

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/ven-1606133328173.png" alt="ven" style="zoom: 50%;" />

![image-20201124002627225](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201124002627225.png?raw=true)



#### 3. Accuracy(정확도)

> 가장 직관적으로 모델의 성능을 나타낼 수 있는 평가 지표이다. 하지만 데이터의 불균형이 있을 때 한쪽 측면만 잘 맞추는 단점이 있다.

![image-20201124002949834](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201124002949834.png?raw=true)



#### 4. F1-Score

> Precision과 Recall의 조화평균이다. 데이터셋이 불균형일 때 자주 사용된다.

![image-20201124003621665](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201124003621665.png?raw=true)





