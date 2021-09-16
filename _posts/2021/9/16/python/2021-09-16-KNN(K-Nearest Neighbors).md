---
layout: post
title: "[python] KNN(K-Nearest Neighbors)"
description: " "
date: 2021-09-16
tags: [파이썬]
comments: true
share: true
---


# KNN(K-Nearest Neighbors)

**최근접 이웃 알고리즘이라 불리며 , 특정 공간내에서 입력과 제일 근접한 k개의 요소를 찾아, 더 많이 일치하는 것으로 분류하는 알고리즘.**

![img](https://t1.daumcdn.net/cfile/tistory/99507F4C5B375A710D)

위의 그림과 같이 파란색 , 주황색으로 구분된 그룹이있다 가정 후 새로 입력된 별이 어떤 그룹에 속해야 할지 정하는 알고리즘이다.

위에 그림은 k = 3 일 때를 나타낸 것이다. 여기서 k 개수가 의미하는 것은 빨간색 원안에 들어갈 요소들의 개수를 의미한다.



**k=1** 일때는 아래와 같다.

![img](https://t1.daumcdn.net/cfile/tistory/99C352455B375B292D)

k = 3 과 k = 1 일 떄의 별이 소속될 그룹이 달라질수 있다.

그러므로 **KNN 알고리즘을 사용할 시 적절한 k값을 찾아 설정해주어야 함.**

