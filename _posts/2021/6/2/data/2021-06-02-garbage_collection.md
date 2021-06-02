---
layout: post
title: "[data] Garbage Collection in Python"
description: " "
date: 2021-06-02
tags: [data]
comments: true
share: true
---

# Garbage Collection in Python

## Garbage Collection, GC 란?

- 메모리 관리 기법 중 하나로 프로그램이 동적으로 할당했던 메모리 영역 중에서 필요없게 된 영역을 해제하는 기능이다.
- 즉, 동적 할당된 메모리 영역 가운데 어떤 변수도 가리키지 않는 메모리 영역을 탐지하여 자동으로 해제하는 기법이다.

### 장점

- GC를 이용하게 되면 프로그래머가 동적으로 할당한 메모리 영역 전체를 완벽하게 관리하지 않아도 된다. 즉, GC를 통해 아래와 같은 버그를 줄이거나 막을 수 있다.
- 유효하지 않은 포인터 접근 : 이미 동적 할당한 메모리를 해제한 영역에 접근하게 되는 버그 이중 해제 : 이미 해제된 메모리를 또 다시 해제하는 오류를 줄일 수 있다. 대표적으로 C에서는 free()를 통해 해제하고 또 다시 free()를 하면 정상 종료 되지 않는다.
- 메모리 누수 : 더이상 사용하지 않는 메모리 영역을 해제하지 않고 남겨진 것이 쌓이게 되면 메모리 누수가 일어난다는 것이다. 이러한 메모리 누수가 지속되면 메모리 고갈로 인해 프로그램이 중단 될 수 있다.

### 단점

- 어떤 메모리를 해제해야 할 지 결정하는데 사용되는 알고리즘에 의해 비용이 든다.
- 객체가 필요없어지는 시점을 프로그래머가 알고 있는 경우에도 GC 알고리즘이 메모리 해제 시점을 추적해야하기에 비용이 들게된다.
- GC가 행동하는 타이밍이나 GC의 점유 시간을 사전에 예측하기 어렵기에 실시간 시스템에는 적합하지 않다. 할당된 메모리가 해제되는 시점을 알 수 없게 된다

<br>

## Python에서 GC

---

Python은 레퍼런스 reference counting 방식으로 GC를 수행해 메모리를 관리하고, reference counting을 사용했을 때 발생할 수 있는 순환 참조 상황을 별도의 GC로 해결한다.

엄밀히 말하면 레퍼런스 카운팅 방식을 통해 객체를 메모리에서 해제하는 행위가 가비지 컬렉션의 한 형태지만 여기서는 순환 참조가 발생했을 때 cyclic garbage collector를 통한 가비지 컬렉션과 레퍼런스 카운팅을 통한 가비지 컬렉션을 구분하여 설명한다.

### 레퍼런스 카운팅

---

모든 객체는 참조 당할 때 레퍼런스 카운터를 증가시키고 참조가 없어질 때 카운터를 감소시킨다. 이 카운터가 0이 되면 객체가 메모리에서 해제한다. 어떤 객체의 레퍼런스 카운트를 보고 싶다면 sys.getrefcount()로 확인할 수 있다.

```python
>>> import sys
>>> a = 'hello'
>>> sys.getrefcount(a)
2
```

여기서 참조횟수가 2인 이유는 첫번째는 variable을 생성하는 것이고 두 번째는 변수 a를 `sys.getrefcount()` 전달할 때이다.

```python
>>> import sys
>>> a = 'hello'
>>> sys.getrefcount(a)
2
>>> b = [a]
>>> sys.getrefcount(a)
3
>>> c = {'first': a}
>>> sys.getrefcount(a)
4
```

variable을 data structure 각 list 또는 dictionary에 추가하면 참조 횟수가 증가한다.

위 코드처럼 list나 dictionary에 추가될 때 a의 참조 횟수가 증가한다.

```python
>>> a = []
>>> a.append(a)
>>> del a
```

- a의 참조 횟수는 1이지만 이 객체는 더 이상 접근할 수 없으며 레퍼런스 카운팅 방식으로는 메모리에서 해제될 수 없다.
- 이러한 유형의 문제를 reference cycle(참조 주기)이라고 하며 reference counting으로 해결할 수 없다.

### Garbage Collector

---

위의 reference cycle 문제를 해결하기위해 garbage collector를 이용하여 메모리를 해제시킬 수 있다.

- 가비지 컬렉터는 메모리의 모든 객체를 추적한다. 새로운 객체는 1세대 부터 3세대까지 총3세대이며 객체는 현재 세대의 가비지 수집 프로세스에서 살아남을 때마다 이전세대로 이동한다.
- 각 세대마다 가비지 컬렉터 모듈에는 임계값 개수의 개체가 있습니다. 객체 수가 해당 임계값을 초과하면 가비지 콜렉션이 콜렉션 프로세스를 trigger(추적)하고 해당 프로세스에서 살아남은 객체는 이전 세대로 옮겨진다.
- 가비지 컬렉터는 내부적으로 generation(세대)와 threshold(임계값)로 가비지 컬렉션 주기와 객체를 관리한다. 세대는 0(young) ~ 2(old)세대로 구분되고 0세대 일수록 더 자주 가비지 컬렉션을 하도록 설계되어있는데 generational hypothesis에 근거한다.

  - 이가설은 대부분은 어린 객체가 오래된 객체보다 해제될 가능성이 훨씬 높다는 가설이다.

  [Generational Hypothesis | Plumbr - User Experience & Application Performance Monitoring](https://plumbr.io/handbook/garbage-collection-in-java/generational-hypothesis)
