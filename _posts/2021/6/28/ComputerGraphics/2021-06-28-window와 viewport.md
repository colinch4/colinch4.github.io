---
layout: post
title: "[그래픽스] window와 viewport"
description: " "
date: 2021-06-28
tags: [graphics]
comments: true
share: true
---

### window와 viewport

#### 정규좌표와 화면좌표

지엘 프로그램이 실행되면서 입력 기본 요소인 정점에 일련의 변환이 가해진다. 이 변환을 대변하는 것이 좌표계 즉 파이프라인 변환 프로세스를 따라가면서 기준 좌표계가 바뀌고, 그때마다 새로운 좌표계를 기준으로 정점 좌표가 바뀐다.

<img src="지엘의 좌표계변화.png">

1. 모델 좌표
   1. 물체별로 모델링에 편하게 설정된 좌표계
2. 전역 좌표
   1. 개별 물체를 모았을 때 이를 한꺼번에 아우를 수 있는 좌표계
3. 시점 좌표
   1. 물체를 바라보는 시점을 기준으로 표현한 좌표계
4. 절단 좌표
   1. 시점으로 부터 보이지 않는 물체를 잘라내기 편하게 설정한 좌표계

나머지 정규, 화면 좌표계는 최종적으로 그림을 화면에 뿌리는 단계, 즉 GLUT의 윈도우 기능이 관여하는 단계다.

모든 3차원 물체는 렌더링 결과 2차원 화면에 뿌려져야한다. 즉, 어느 순간에 3차원 좌표에서 2차원 좌표로의 변환이 필요하다. 이 변환은 절단 -> 정규 좌표계로 넘어오면서 이루어진다. 여기서 정규좌표는 1을 기준으로 하는 2차원 좌표다.

즉 정규화는 어떤 값을 1을 기준으로 하여 상대적으로 표시하는 행위다. 따라서 정규화를 거치면 모든 정점 좌표는 1보다 작은 값으로 바뀐다.

<img src="https://t1.daumcdn.net/cfile/tistory/9915904F5AE9BEAF10">

위에서 소수 정밀도를 지니게 된 정규 좌표는 정수 정밀도의 화면 좌표로 바뀐다.

여기서 화면 좌표는 window 즉 창의 크기를 얘기하는데
위의 그림의 화면 좌표의 방식으로 x축은 오른쪽으로 y축은 아래로 향한다. 다만 이 좌표계 설정은 상대적인 것이므로 소프트웨어나 컴파일러등에 따라 달라질 수 있다.

정규좌표 -> 화면좌표의 계산과정은 굉장히 쉽다.

1024 _ 768의 window에서 좌표 계산이 이루어진다면 1,023 _ ((정규좌표) + 1.0))\* 0.5가 된다.

즉 1023 부분을 제외한 나머지가 미리 계산되면 출력 장치의 해상도 차이에 빠르게 적응할 수 있다.

#### viewport

뷰포트는 윈도우 내부에 설정한 작은창을 말한다.

<img src="http://jerome.jouvie.free.fr/opengl-tutorials/tutorials/Tutorial8-Viewport.png">

프로그래머가 별도로 뷰포트를 정의하지 않으면 기본 설정에 의해 묵시적으로 현재 윈도우 전체가 하나의 뷰 포트로 간주된다. 이 경우 왜곡이 일어나기 쉽다.
