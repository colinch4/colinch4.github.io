---
layout: post
title: "[데이터사이언스] 모두를 위한 딥러닝 강좌 시즌 1 by 김성훈 교수"
description: " "
date: 2021-06-17
tags: [개발]
comments: true
share: true
---

## 모두를 위한 딥러닝 강좌 시즌 1 by 김성훈 교수

홍콩과기대 김성훈 교수의 [유투브 강의](https://www.youtube.com/watch?v=BS6O0zOGX4E&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm)를 뒤늦게 몰아보고 있다. 생각보다 훨씬 초급자 수준에 맞추어져 있어서 진입장벽이 매우 낮다고 하겠다. 영상목록의 제목처럼, 정말 "모두를 위한" 강의가 아닌가 싶다.

## 강의관련 요약

초반부는 머신러닝에 관한 간단한 소개 정도로 요약할 수 있다. 알파고가 이세돌 기사를 이겼던 이후, 광풍이 불었던 (현재도 진행중인) 시기에 만들어진 강의여서 모두들 장미빛을 안고 강의를 듣고 있을 것 같다. 최근에 IBM 왓슨의 의료 프로젝트가 주춤하는 모양새인데, 너도나도 할 것없이 모여들었던 기술 투자에 대한 조정기가 아닐까 싶다.

이 강의는 lec과 lab 파트로 구분되는데, lec에서는 수식이나 개념을 설명하고, lab 파트에서는 구글 텐서플로우 코드로 구현한 것을 소개한다.

Lec 02에서는 선형회귀를 소개한다.

Lec 03에서는 cost 함수를 소개하고, cost 함수를 최소화함으로써 선형회귀 문제를 푼다는 걸 설명한다.

Lec 04에서는 행렬을 이용해서 여러가지 변수를 갖는 회귀식을 소개한다.

Lec 05에서는 Logistics 회귀를 소개한다. 데이터셋의 극치값이 추가됨에 따라 판별식이 달라지는 것을 방지한다. 시그모이드를 소개하고, 이 이후 Hypothesis가 선형식에서 로그회귀로 바뀐다. 로그회귀의 cost 함수는 로그형태를 취하는 형식으로 달라진다.

Lec 06에서는 softmax를 소개하는데, 시그모이드함수를 통해 0-1사이의 출력값을 가지게 되었고, 여러개의 결과(Y)에 대해서 값을 가지게 되는데, softmax를 통해 확률 값으로 변환한다. 선형회귀 모형의 cost 함수는 cross-entropy를 이용한다. 이전에 사용했던 로그회귀의 cost 함수가 사실 크로스 엔트로피 함수였다. D(S, L) = sum(L*los(S)) 로 쓴다. `one-hot`를 다루는 방법은 lab강의에서 다룬다. 분류를 할 때, 분류의 값이 `[1,2,3,4]`와 같이 되어 있을텐데, 이를 `[1 0 0 0], [0 1 0 0], [0 0 1 0]` 등으로 바꾸어 주는것이다. 텐서플로우 코드에서는 랭크가 하나 늘기 때문에, `tf.one_hot` 처리 후, `tf.reshape`를 해주어야 한다.

Lec 07에서는 학습 rate, 오버피팅, 일반화(Regulation)를 소개한다. 학습 rate는 0.01정도로 시작하는데, 발산여부와 수렴속도를 살펴보고 조정할 수 있다. 특성 변수가 큰 범위를 가지면, 학습이 잘 안되는 경우가 있다. 이럴 때, Nomalization이 필요하다. 그 중 하나가 Standardization인데, `x_std[:, 0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()`으로 쓸 수 있다. 정규분포라고 가정하면, 시그마 거리를 구하는 것이다. 오버피팅은 피쳐수를 줄인다던지, 데이터 자료수를 늘리거나, 일반화를 통해서 완화할 수 있다. cost 함수에 전체값의 합을 넣어주어 일반화하는것이다.

Lab 07에서 용어 정리도 하는데, `epoch`는 전체 학습데이터셋을 한번 다 돌리는 횟수, 유전 알고리즘의 세대와 비슷한 개념, `batch size`는 데이터셋이 커서 그 샘플링할 셋의 크기, `iterations`은 배치 사이즈에 따라 반복 횟수로 정의된다.

Lec 08에서는 딥러닝의 개념을 소개하고 있다. 초창기 인간의 뇌신경을 따라 만든 인공신경망은 XOR 문제를 풀 수 없었다. 마빈 민스키 교수가 MLP을 통해서 풀 수 있으나, 이를 학습할 수가 없다고 강변하였다. 1974년, 1982년 Paul Werbos, 1986년 Hinton에 의해서 backpropagation이 소개되었다. 또한 LeCun 교수가 컨볼루셔날 뉴럴 네트워크(CNN)을 소개하여 발전이 꽤 있었다. 문자인식 기술에 90% 이상의 인식율을 보였다고 한다. 하지만 1990년대 중반, 레이어가 많아지자 역전파가 제대로 작동하지 않았고, SVM, RandomForest 등이 간단하지만 더 나은 성능을 보여주면서 다시 역사의 그림자 속으로 들어가게 되었다.

캐나다의 CIFAR는 당장의 활용성이 떨어지더라도 펀딩을 지속적으로 하였는데, 역전파를 재발견한 Hinton 교수가 1987년 캐나다로 옮겨가면서 이 재단의 후원을 받았다. 그리고 2006년 Hinton교수의 "A fast learning algorithm for deep belief nets"와 2007년 Yoshua Bengio 교수의 "Greedy Layer-Wise Training of Deep Networks"라는 두 논문이 발표되었다. 2006년 논문은 초기 가중치에 따라 결과의 성능이 크게 달라짐을 밝혔고, 2007년 논문에서는 딥러닝을 통해 다양한 문제를 잘 풀어낼 수 있는 가능성을 보여주었다. 이때 딥러닝으로 리브랜딩이 되었다. 그 이후는 잘 알다시피, ImageNet에서 큰 성과를 보였고, 알파고, 음성인식, 유투브 자막 자동생성, 자율주행 등의 성과를 보이게 되었다.

Lab 08에서는 numpy의 인덱스 사용법을 설명하고 있는데, 일반적인 내용이므로 패스. rank는 괄호수를 세면 된다. Axis는 바깥괄호부터 0, 1, 2 이렇게 센다. 브로드캐스팅은 쉐입이 다를 경우, 자동으로 쉐입을 맞춰주는데, 잘 모르면 쉐입을 맞추어서 계산하자. 변수를 추가할 때는 stack() 메서드를 이용할 수 있다.

Lec 09에서는 XOR를 구현하기 위해서 NN을 설명한다. 반가산기처럼 뉴럴을 중첩해서 계산할 수 있으며, 초기값을 잘 정해주면 풀린다. 이 문제를 풀기 위해서 가중치를 잘 정해주어야 하는데, 민스키 교수가 지적했듯이 계산하기가 어렵다. 그래서 역전파 방법이 필요하다. forward propagation은 값을 넣어서 계산하면 되는데, back propagation은 편미분을 해서 구한다. 편미분값은 네트워크를 역순으로 따라오면서, 그 미분값을 계속 곱하면 되는데, 결국은 체인룰과 같은 형태가 되는것이다. 미분 역시 수치해석으로 풀이 가능하다. 미분을 설명하기 위해서 상당시간을 소요하는데, 공학전공자면 스킵할 수 있다.

Lab 11-1에서는 CNN를 이용하여 3x3 이미지 학습을 실습한다. `(1, 3, 3, 1)`에서 첫번째 숫자는 총 샘플링 갯수이다. 필터는 h, w, channel, filter 순서로 적는다. `padding`를 `same`으로 지정하면, 사이즈를 맞추기 위해서 마지막 행과 마지막 열에 0를 채운다. 채널을 여러개로 줄 수도 있다. 채널이 마지막 디멘션이므로, 리스트 형태를 갖는다. `max_pool`를 많이 이용하는데, 동일하게 윈도우가 움직이면서 연산하고, 최대값을 선택하게 된다. `strides` 역시 주어진 입력의 차원과 같은 순서를 갖게 되어, 2번째와 3번째 숫자가 이미지에서 몇칸씩 움직일지를 결정한다. `padding="same"`과 `(1,2,2,1)`를 입력하면, 이미지가 절반 사이즈로 줄어든다. 이미지를 출력하는 코드는 설명을 생략한다.

Lab 11-2, CNN은 컨볼루션 레이어와 풀링으로 2번 반복하고, 마지막에 FC(fully connected) 레이어를 붙여준다. 마지막에 FC에 붙일 때, 7x7x64 (7x7 64 filter)를 (?, 3136)인 일차원 벡터로 `reshape()`해준다. 98% 정도 정확도가 나오는데, 한단씩 더 추가해서 좀 더 깊은 CNN를 만들면, 99%까지 성능이 올라간다. 이 때, dropout를 지정해준다. 학습할 때는 dropout를 0.5 에서 0.7정도로 주고, test할 때는 1를 쓰도록 한다.

