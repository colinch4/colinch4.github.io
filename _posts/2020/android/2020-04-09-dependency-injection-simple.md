---
layout: post
title: "[Android] Dependency Injection이란?"
date: 2020-04-09 15:30
category: 
author: colinch4
tags: [Android]
description: "객체 간의 의존관계를 객체-객체 가 아닌 외부에서 객체를 생성하고 전달해 줌으로 써 객체간의 의존성 제거 및 결합도를 낮추는 것"
comments: true
share: true
---



객체 간의 의존관계를 객체-객체 가 아닌 외부에서 객체를 생성하고 전달해 줌으로 써 객체간의 의존성 제거 및 결합도를 낮추는 것

## 장점

1.  모듈간의 의존성이 낮아져 유지보수에 좋다
2.  모듈간의 의존성이 낮아져 코드 재사용이 좋다. (기능별로 분리를 잘 한 경우)
3.  테스트 하기 좋다.

## 설명

Android는 context의 영향을 많이 받는 플랫폼이라고 할 수 있습니다. 가장 큰 예로 Activity LifeCycle에 따라 자원을 생성하고 사용 할 수 있습니다. 즉 Activity, Fragment내에서 선언되고 사용되는 Instance 들은 Activity, Fragment의 영향을 받는다는 말입니다.

Instance 생성 시 내부 환경의 영향을 받는다면, 같은 Instance 라도 다른 환경에서 다르게 동작 할 수 있습니다. 하지만 항상 같은 환경에서만 Instance를 생성하고, Activity나 Fragment 에서는 생성된 Instance를 받아서 사용만 한다면 내부 환경과 상관없이 같은 동작을 하며, 범용적으로 재사용 할 수 있습니다. 이런 개념을 DI(Dependency Injection)이라고 합니다.

![](https://miro.medium.com/max/60/1*6z72NaDEXS1gufJ16MBZHQ.png?q=20)

![](https://miro.medium.com/max/1024/1*6z72NaDEXS1gufJ16MBZHQ.png)

Component 는 Activity A와 Activity B에게 각각 필요한 Instace들을 선언합니다. Component 는 요청한 Instance들을 Injection 해줍니다. 그림처럼 Activity A와 ActivityB는 내부에서 instance를 생성하지 않고 Component를 통해 필요한 Instance들을 주입 받습니다.

이렇게 함으로 써 instance들은 Activity 의존성이 느슨해지며 어떤 Activity가 되더라도 같은 instance들을 주입 받습니다.