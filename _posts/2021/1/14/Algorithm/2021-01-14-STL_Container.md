---
layout: post
title: "[알고리즘] STL Container"
description: " "
date: 2020-01-14
tags: [알고리즘]
comments: true
share: true
---


Container 목록 및 특징은 완성될 때 까지 수시로 추가합니다.

STL은 Standard Template Library의 약자로, **알고리즘, 컨테이너, 함수, 이터레이터** 로 이루어져 있다.



## Pair

자료형 pair를 사용하면 두 자료형 V1, V2를 한꺼번에 묶을 수 있다. Pair이라는 이름과 같이 반드시 두 개씩 묶어야 한다. 첫 번째 자료는 `first `, 두 번째 자료는 `second` 로 접근할 수 있다. 

#include <utility>에 존재하지만 다른 헤더파일들에 이미 존재하고 있기 때문에 따로 include하는 일은 없다. pair을 선언하는 방법은 `생성자` 와 `make_pair` 를 사용하는 방법 두 가지가 있다.

```c++
// Pair를 선언하는 다양한 방법들

pair<int, int> p1;
cout << p1.first << ' ' << p1.second; // 0 0

p1 = make_pair(10,20);
cout << p1.first << ' ' << p1.second; // 10 20

p1 = pair<int, int>(30,40);
cout << p1.first << ' ' << p1.second; // 30 40

pair<int, int>(50,60) p2;
cout << p2.first << ' ' << p2.second; // 50 60

// Pair안에 Pair를 또 선언할 수 있다.
pair<pair<int,int>, pair<int, char>> p3;
make_pair(make_pair(10,20), make_pair(30,'forty'));
cout << p3.first.first << ' ' << p3.first.second; // 10 20
cout << p3.second.first << ' ' << p3.second.second; // 30 forty
```



## Tuple

기존의 Pair가 두 개의 자료형을 묶을 수 있었다면 Tuple은 여러 개를 묶을 수 있다.

접근방식은 .first .second .third …가 아닌, get 을 이용해 인덱스에 접근하여야 한다.tuple을 사용하기 위해선 #include <tuple>을 정의해야 한다. tuple을 선언하는 방식은 다음과 같다.

```c++
tuple<int, int, int> t1 = make_tuple(1,2,3);
cout << get<0>t1; // 1
cout << get<1>t1; // 2
cout << get<2>t1; // 3

// 주의!!! get<> 의 꺽새 사이에 변수는 넣을 수 없다. 따라서 for문을 돌리는 것이 불가능하다.
```



## Vector

vector는 길이를 변경할 수 있는 배열이다. vector를 사용하려면 코드 상단에 #include <vector> 를 선언해주면 된다. 예제를 통하여 알아보자. 
