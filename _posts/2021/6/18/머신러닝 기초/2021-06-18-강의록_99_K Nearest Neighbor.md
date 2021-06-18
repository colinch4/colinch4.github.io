---
layout: post
title: "[머신러닝 기초] 99. K-Nearest Neighbor"
description: " "
date: 2021-06-18
tags: [머신러닝]
comments: true
share: true
---

## K-Nearest Neighbor
1. [개요](#1장-개요)   
2. [KNN 알고리즘](#2장-KNN-알고리즘)   
3. [거리측정 방법](#3장-거리측정-방법)   
4. [KNN 특징](#4장-KNN-특징)   
5. [Weighted KNN](#5장-Weighted-KNN)   

### 1장 개요
- 분류 및 예측을 위한 모델
  - Model-based Learning : 데이터로부터 모델을 생성하여 분류/예측 진행
  - Instance-based Learning : 별도의 모델 생성 없이 인접 데이터를 분류 / 예측에 사용

- Nearest Neighbors 
  - 1-nearest neighbors : 새로운 데이터와 가장 가까운 1개의 데이터 정의
  - 3-nearest neighbors : 새로운 데이터와 가장 가까운 3개의 데이터 정의
    - ![캡처](https://user-images.githubusercontent.com/43491168/112488355-cf888500-8dc0-11eb-8a29-277d71688ad7.PNG)
  - ![캡처](https://user-images.githubusercontent.com/43491168/112488708-25f5c380-8dc1-11eb-9d2a-3bf7a6c209c4.PNG)

### 2장 KNN 알고리즘
- KNN 특징
  - Instance-based Learning
  - Memory-based Learning : 모든 데이터를 메모리에 저장한 후, 이를 바탕으로 예측
  - Lazy Leaning : 데스팅 데이터가 들어와야 비로서 작동한는 게으른 알고리즘

- KNN 알고리즘
  - Classification
    - ![캡처](https://user-images.githubusercontent.com/43491168/112489602-f0050f00-8dc1-11eb-8358-2bb1dd7390d2.PNG)
  - Regression
    - ![캡처](https://user-images.githubusercontent.com/43491168/112489800-2478cb00-8dc2-11eb-9ec6-15aa4e2b978a.PNG)

- KNN 하이퍼파라미터
  - k : 인접한 학습 데이터를 몇 개까지 탐색할 것인가
    - k가 작을 경우 : 데이터의 지역적 특성을 과반영(Overfitting)
    - k가 클 경우 : 다른 범주의 개체를 너무 많이 포함(Underfitting)
      - 일정 범위 내로 k를 조정(gride search) : 분류(오분류율), 예측(오차 제곱합)
      - ![캡처](https://user-images.githubusercontent.com/43491168/112490760-019ae680-8dc3-11eb-9aed-69753151d55a.PNG)

  - Distance Measures : 데이터 간 거리측정 방법
    - 데이터 내 변수들이 각기 다른 범위, 분산 등을 가질 수 있으므로 정규화(or 표준화)가 중요

### 3장 거리측정 방법
- Euclidean Distance
  - ![캡처](https://user-images.githubusercontent.com/43491168/112491335-8ede3b00-8dc3-11eb-8c6c-e3445df44e1b.PNG)
  - x = x1, y = x2

- Manhattan Distance
  - ![캡처](https://user-images.githubusercontent.com/43491168/112491730-ed0b1e00-8dc3-11eb-99c0-4b56c9792a59.PNG)

- Manhalanobis Distance
  - ![캡처](https://user-images.githubusercontent.com/43491168/112491794-001dee00-8dc4-11eb-9f08-95d88f1add93.PNG)
    - 변수 내 분산, 변수 간 공분산을 모두 반영한 거리 계산
    - 데이터의 covariance matrix가 identity matrix인 경우는 Euclidean distance와 동일
  - Example : 
    - ![캡처](https://user-images.githubusercontent.com/43491168/112492686-d0bbb100-8dc4-11eb-8ede-9735809e394a.PNG)

- Correlation Distance
  - pearson Correlation
    - ![캡처](https://user-images.githubusercontent.com/43491168/112492911-06f93080-8dc5-11eb-8703-5f59d001f8cf.PNG)
      - 시그널 형태의 데이터에서 거리비교에 주로 사용
      - 데이터 간 Pearson correlation을 거리측도로 사용하는 방식으로, 데이터 패턴의 유사도를 반영할 수 있음
  
  - Spearman Rank Correlation
    - 데이터의 rank를 이용하여 correlation distance를 계산하는 방식
    - ![캡처](https://user-images.githubusercontent.com/43491168/112493269-5b9cab80-8dc5-11eb-88ee-86d00eff9251.PNG)
      - Example : 
        - ![캡처](https://user-images.githubusercontent.com/43491168/112493558-9c94c000-8dc5-11eb-8d00-29af9161b0a8.PNG)

### 4장 KNN 특징
- 장단점
  - 장점
    - 학습 데이터의 수가 많을 경우 효과적
    - 데이터 내 노이즈에 영향을 크게 받지 않음
    - Manhalanobis Distance와 같이 분산을 고려할 경우 결과가? 강건함
  - 단점
    - k값을 설정해야함
    - 어떤 거리 척도가 적합한지 불분명(데이터 특성에 맞게 임의 선택해야 함.)
    - 새로운 관측치와 각각의 학습 데이터 간 거리를 모두 측정해야함(오래걸림.)
  - 요약
    - 단순한 접근방식으로 예측
    - 특정 형태 모델없이 학습 데이터 내 유사한 관측치를 바탕으로 예측
    - Weighted KNN 알고리즘으로 데이터의 가중치를 고려할 수 있음

### 5장 Weighted KNN
- 새 데이터와 기존 학습 관측치 간의 거리를 가중치로 하여 예측
- ![캡처](https://user-images.githubusercontent.com/43491168/112494509-76235480-8dc6-11eb-9389-152ec5936e06.PNG)



