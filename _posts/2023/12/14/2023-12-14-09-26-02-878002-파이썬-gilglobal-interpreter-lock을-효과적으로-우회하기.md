---
layout: post
title: "[python] 파이썬 GIL(Global Interpreter Lock)을 효과적으로 우회하기"
description: " "
date: 2023-12-14
tags: [python]
comments: true
share: true
---

## 개요

파이썬은 GIL(Global Interpreter Lock)라는 메커니즘으로 인해 한 번에 하나의 스레드만이 파이썬 바이트코드를 실행할 수 있습니다. 이로 인해 멀티코어 시스템에서도 병렬 처리가 제대로 이루어지지 않고 성능이 저하될 수 있습니다. 이러한 문제를 해결하기 위해 GIL을 우회하는 여러 방법이 존재합니다.

## GIL 우회 기술

### 1. 멀티 프로세스

파이썬의 `multiprocessing` 모듈을 사용하여 별도의 프로세스를 생성하고 각 프로세스에서 병렬로 작업을 처리하는 방법이 있습니다. 이는 GIL이 각 프로세스마다 별도로 적용되기 때문에 병렬 처리가 가능해집니다.

```python
from multiprocessing import Process

def foo():
    # 작업 수행

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=foo)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

### 2. Cython 사용

Cython을 사용하여 파이썬 코드를 C 혹은 C++로 변환하면 GIL을 우회할 수 있습니다. Cython은 C 언어와 파이썬 언어를 혼합한 하이브리드 언어로, C 언어의 성능을 높이고 파이썬 코드와의 호환성을 제공합니다.

```python
# cython 코드 예시
cdef int a = 0
for i in range(1000000):
    a += i
```

### 3. Jython 사용

Jython은 파이썬 인터프리터를 자바 바이트코드로 번역하는 도구입니다. 따라서 JVM(Java Virtual Machine) 위에서 동작하며, GIL 이슈가 없어 병렬 처리가 가능합니다.

## 결론

파이썬의 GIL은 멀티스레드 환경에서 성능 저하를 초래할 수 있지만, 여러 우회 기술을 통해 이를 극복할 수 있습니다. 선택한 기술에 따라 동시성과 병렬성을 효과적으로 활용하여 파이썬 애플리케이션의 성능을 향상시킬 수 있습니다.

참고문헌:
- https://docs.python.org/3/library/multiprocessing.html
- https://cython.org/
- https://www.jython.org/