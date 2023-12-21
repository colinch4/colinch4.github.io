---
layout: post
title: "[python] 파이썬 GIL (Global Interpreter Lock) 이해하기"
description: " "
date: 2023-12-21
tags: [python]
comments: true
share: true
---

파이썬은 GIL (Global Interpreter Lock)이라는 특별한 기능을 가지고 있습니다. GIL은 파이썬 인터프리터가 한 번에 하나의 스레드만을 실행하도록 강제하는 메커니즘입니다. 이 기능은 파이썬의 멀티스레딩 성능을 제한하지만, 이해하기 쉽고 안전한 다른 이점을 제공합니다.

## GIL이 필요한 이유

GIL은 파이썬이 안전하게 멀티스레딩을 지원하기 위해 필요합니다. 파이썬의 많은 내장 객체 및 모듈들은 스레드 간 안전하지 않기 때문에, GIL은 이를 보호하고 교착 상태를 방지합니다. 따라서, GIL은 파이썬의 안정성을 유지하는 데 중요한 역할을 합니다.

## GIL의 영향

파이썬의 GIL은 CPU-bound 작업의 성능에 영향을 줄 수 있습니다. GIL은 하나의 스레드만이 실행되도록 강제하기 때문에 멀티코어 시스템에서 병렬 처리를 제한할 수 있습니다. 하지만 I/O-bound 작업에는 큰 영향이 없으며, 이러한 작업에서는 멀티스레딩이 여전히 효과적일 수 있습니다.

## GIL 우회하기

GIL을 우회하는 방법 중 하나는 `multiprocessing` 모듈을 사용하여 별도의 프로세스를 생성하는 것입니다. 또한, C 확장 라이브러리를 사용하여 GIL을 우회하는 방법도 있습니다.

```python
import multiprocessing

def worker():
    # 작업 수행
    pass

if __name__ == '__main__':
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()
```

## 요약

파이썬의 GIL은 멀티스레딩 작업을 제한하지만, 파이썬의 안정성을 유지하는 중요한 요소입니다. GIL을 우회하는 방법을 적절히 활용하면, 멀티스레딩의 성능을 최적화할 수 있습니다.

참고 문헌:
- https://realpython.com/python-gil/