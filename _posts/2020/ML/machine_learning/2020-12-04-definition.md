---
layout: post
title: "[머신러닝] AI, ML, DL 분류"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

## AI, ML, DL 분류

> AI, Machine Learning, Deep Learning 과 관련한 용어들을 정리한다.



## AI(Artifical Intelligence)

> 한국말로 **인공지능**으로  인간이 가지고 있는 학습능력, 응용력, 추론능력 등을 컴퓨터를 통해서 구현하고 하는 가장 포괄적인 개념이다.





## ML(Machine Learing)

> 한국말로 **기계학습**으로 AI를 구현하는 하나의 방법론이다.
>
> **데이터**를 이용해서 데이터의 특서오가 그 결과를 바탕으로 미지의 데이터에 대한 미래결과를 **예측**하는 프로그래밍 기법이다.



#### ML이 필요한 이유

> ML은 Explicit program(rule based program)의 한계 때문에 고안되었다.
>
> 어떠한 프로그램들은 rule(조건)들이 너무 많기 때문에 Explicit program으로 구현하기 힘들기 때문이다. 예를 들어 대출 spam 문자를 걸러내기 위해 **대출** 이라는 단어를 설정해두면 **대^^출** 같은 단어는 걸러내기 힘들다.
>
> 따라서 프로그램 자체가 데이터 기반으로 학습을 통해 배우는 능력을 가지는 프로그램을 지칭한다.



#### ML의 분류

* **지도학습**(Supervised Learning)  : 데이터와 정답(label)을 이용해서 데이터의 특성과 분포를 학습하고 미래 결과를 예측하는 방법이다.

  *  회귀(Regression) : Linear Regression, Logistic Regression
  * Classification(분류): binary classification, multinomial classification

* 비지도학습(Unsupervised Learning) : 정답(label)이 없는 데이터가 사용되는것이 지도학습과의 가장 큰 차이점이고 특성과 분포를 이용해서 Grouping 하는 **Clustering(군집화)** 하는데 주로 사용된다.

* 준지도학습(Semi-Supervised Learning) : 데이터 일부분만이 정답(label)을 갖고 있는 경우이다. ex) Google Photos

* 강화학습(Reinforcement Learning) : 게임쪽에서 많이 사용되는 학습방법을 사용하면 Agent, Environment, Action, Reward 개념을 이용한다.

  



#### 알고리즘 종류

* Regression(Linear Regression, Logistic Regression)
* SVM(Support Vector Machine)
* Random Forest
* Descision Tree
* Neural Network(신경망)
* Clustering
* Reinforcement Learning



## DL(Deep Learning)

> ML의 한 부분으로 Neural Network를 이용해서 학습하는 알고리즘의 집합이다.



#### 알고리즘 종류

* CNN
* RNN
* LSTM
* GAN





## 참고

AI > ML > DL





