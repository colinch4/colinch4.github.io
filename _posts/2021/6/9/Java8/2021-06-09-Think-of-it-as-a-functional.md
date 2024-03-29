---
layout: post
title: "[Java8] 함수형 관점으로 생각하기"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

함수형 관점으로 생각하기
------------------------

### 요약

-	공유된 가변 자료구조를 줄이는 것은 장기적으로 프로그램을 유지보수하고 디버깅하는데 도움이 된다.
-	함수형 프로그래밍은 부작용이 없는 메서드와 선언형 프로그래밍 방식을 지향한다.
-	함수형 메서드는 입력 인수와 출력 결과만 갖는다.
-	같은 인수값으로 함수를 호출했을 때 항상 같은 값을 반환하면 참조 투명성을 갖는 함수다. while 루프 같은 반복문은 재귀로 대체할 수 있다.
-	자바에서는 고전 방식의 재귀보다는 꼬리 재귀를 사용해야 추가적인 컴파일러 최적화를 기대할 수 있다.
