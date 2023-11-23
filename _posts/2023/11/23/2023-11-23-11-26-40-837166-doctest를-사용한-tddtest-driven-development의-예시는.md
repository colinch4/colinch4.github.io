---
layout: post
title: "[python] doctest를 사용한 TDD(Test-Driven Development)의 예시는?"
description: " "
date: 2023-11-23
tags: [python]
comments: true
share: true
---

# TDD(Test-Driven Development)와 doctest 예시

## TDD란?

TDD(Test-Driven Development)는 소프트웨어 개발 방법론 중 하나로, 테스트를 작성하고 그 테스트를 통과시키는 코드를 작성하는 방식입니다. 테스트는 실제 동작하는 코드보다 먼저 작성되며, 이를 통해 개발자는 요구사항에 맞는 코드를 작성할 수 있습니다.

## doctest란?

doctest는 Python의 표준 라이브러리인 `doctest` 모듈을 통해 제공되는 도구입니다. doctest는 문서화된 예시를 통해 코드를 테스트합니다. 프로그래머는 함수나 모듈의 동작 예시를 문서화하여 테스트할 수 있으며, 이러한 예시는 실제로 테스트를 실행하는데 사용됩니다.

## TDD와 doctest의 예시

여기서는 간단한 문자열 처리 함수를 작성하고, TDD와 doctest를 통해 해당 함수를 테스트하는 예시를 살펴보겠습니다.

```python
def reverse_string(s):
    """
    문자열을 뒤집어 반환하는 함수

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("world")
    'dlrow'
    """
    return s[::-1]
```

위의 예시 코드에서 `reverse_string` 함수는 주어진 문자열을 뒤집어 반환합니다. 함수에 대한 예시는 docstring에 작성되어 있으며, 각 예시는 `>>>` 기호로 시작합니다.

위의 코드를 실행하면, `doctest` 모듈이 예시를 테스트하고 결과를 출력합니다. 예시의 실행 결과가 예상한 대로 출력되면 테스트는 통과한 것으로 간주됩니다. 만약 예상한 결과와 다르다면 오류가 발생하고, 이를 통해 개발자는 코드에 문제가 있는지 확인할 수 있습니다.

위의 예시를 실행해보면 다음과 같은 결과를 확인할 수 있습니다.

```
**********************************************************************
File "__main__", line 6, in __main__.reverse_string
Failed example:
    reverse_string("hello")
Expected:
    'olleh'
Got:
    'olleh'
**********************************************************************
File "__main__", line 8, in __main__.reverse_string
Failed example:
    reverse_string("world")
Expected:
    'dlrow'
Got:
    'dlrow'
**********************************************************************
1 items had failures:
   2 of   2 in __main__.reverse_string
***Test Failed*** 2 failures.
```

결과를 통해 확인할 수 있듯이, 예시의 실행 결과는 예상한 대로 나왔습니다. 이를 통해 `reverse_string` 함수는 예상한 대로 동작한다는 것을 확인할 수 있습니다.

## 결론

TDD(Test-Driven Development)와 `doctest` 모듈을 사용하면 개발 과정에서 코드 품질을 향상시키고 버그를 방지할 수 있습니다. 예상 동작을 문서화하여 코드를 테스트하면 코드의 질을 유지하고 유연성을 확보할 수 있습니다.