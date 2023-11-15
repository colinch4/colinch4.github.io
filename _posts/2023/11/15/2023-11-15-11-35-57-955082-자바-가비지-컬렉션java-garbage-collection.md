---
layout: post
title: "[java] 자바 가비지 컬렉션(Java garbage collection)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

가비지 컬렉션(Garbage Collection)은 자바 가상 머신(JVM, Java Virtual Machine)의 주요 기능 중 하나로, 자동적으로 메모리 관리를 담당합니다. 가비지 컬렉션은 프로그램에서 더 이상 사용되지 않는 객체를 파악하고, 해당 객체의 메모리를 자동으로 해제하여 메모리 누수(memory leaks)를 방지합니다.

## 가비지 컬렉션 프로세스

자바에서 가비지 컬렉션은 다음과 같은 프로세스를 통해 이루어집니다.

1. **객체 생성**: 프로그램에서 새로운 객체가 생성됩니다.
2. **객체 사용**: 생성된 객체가 프로그램에서 사용됩니다.
3. **객체 참조**: 생성된 객체에 대한 참조(reference)가 다른 객체나 변수에 할당됩니다.
4. **객체 사용 종료**: 생성된 객체가 더 이상 사용되지 않습니다.
5. **객체 참조 해제**: 객체에 대한 참조가 없어집니다.
6. **가비지 컬렉션 실행**: 가비지 컬렉션이 실행되면서 더 이상 사용되지 않는 객체의 메모리를 해제합니다.

## 가비지 컬렉션 알고리즘

가비지 컬렉션은 다양한 알고리즘을 사용하여 메모리를 관리합니다. 대표적인 알고리즘으로는 다음과 같은 것들이 있습니다.

- **Mark and Sweep**: 모든 객체를 순회하면서 사용되는 객체를 표시(mark)하고, 표시되지 않은 객체는 해제(sweep)합니다.
- **Copying**: 메모리를 두 영역으로 나누고, 사용되는 객체를 하나의 영역에 복사하고 사용되지 않는 객체를 해제합니다. 영역 전환시에는 객체의 참조를 업데이트해야합니다.
- **Generational**: 객체를 세대(generation)로 분류하고, 각각 다른 가비지 컬렉션 알고리즘을 적용합니다. 자주 사용되는 객체는 더 자주 가비지 컬렉션을 실행합니다.

## 가비지 컬렉션의 장단점

가비지 컬렉션의 장점은 다음과 같습니다.

- 메모리 관리를 자동으로 처리해줌으로써 개발자가 수동으로 메모리를 해제하는 번거로움을 줄여줍니다.
- 메모리 누수를 방지하여 프로그램의 안정성과 성능을 향상시킵니다.

하지만, 가비지 컬렉션은 다음과 같은 단점도 가지고 있습니다.

- 가비지 컬렉션 실행 시간이 예측하기 어렵기 때문에, 프로그램 실행 속도가 일정하지 않을 수 있습니다.
- 가비지 컬렉션 실행 시에는 프로그램이 멈추기 때문에, 실시간성이 중요한 애플리케이션에는 부적합할 수 있습니다.

## 참고 자료

- [자바 가비지 컬렉션 개념 및 동작 방식](https://d2.naver.com/helloworld/1329)
- [Java Garbage Collection](https://www.baeldung.com/java-garbage-collection)
- [Understanding Garbage Collection in Java](https://stackify.com/understanding-garbage-collection-in-java/)
- [Garbage Collection in Java](https://www.journaldev.com/2856/java-garbage-collection)