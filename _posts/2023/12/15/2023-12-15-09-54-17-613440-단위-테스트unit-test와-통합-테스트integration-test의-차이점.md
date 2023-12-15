---
layout: post
title: "[python] 단위 테스트(Unit Test)와 통합 테스트(Integration Test)의 차이점"
description: " "
date: 2023-12-15
tags: [python]
comments: true
share: true
---

단위 테스트(Unit Test)와 통합 테스트(Integration Test)는 소프트웨어 테스팅의 중요한 부분으로, 각각의 특징과 목적이 다릅니다. 이번 글에서는 두 테스트 방법의 차이점을 살펴보겠습니다.

## 단위 테스트(Unit Test)

**단위 테스트(Unit Test)**는 코드의 작은 부분을 테스트하는 것으로, 보통 함수나 메서드와 같은 개별적인 유닛(unit)을 테스트합니다. 단위 테스트는 모듈이나 클래스 내부의 각각의 구성 요소가 올바로 작동하는지 확인합니다. 이를 통해 개발자는 작은 단위가 독립적으로 올바로 작동하는지 확인할 수 있습니다.

예를 들어, 다음은 Python unittest를 사용하여 간단한 함수의 단위 테스트를 하는 예제입니다.

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

if __name__ == '__main__':
    unittest.main()
```

## 통합 테스트(Integration Test)

반면에, **통합 테스트(Integration Test)**는 각각의 독립된 단위들을 결합하여 전체 시스템이 예상대로 동작하는지를 검증합니다. 통합 테스트는 시스템의 다양한 구성 요소들 간의 상호 작용을 확인하여 시스템이 올바로 통합되었는지를 확인합니다.

예를 들어, 다음은 Python의 `requests` 라이브러리를 사용하여 웹 서비스의 통합 테스트를 하는 예제입니다.

```python
import requests
import unittest

class TestAPICalls(unittest.TestCase):
    def test_get_user_info(self):
        response = requests.get('https://api.example.com/user/123')
        self.assertEqual(response.status_code, 200)
        # 추가적인 검증 로직 ...

if __name__ == '__main__':
    unittest.main()
```

## 결론

**단위 테스트**는 개별적인 코드의 작은 부분을 중심으로, **통합 테스트**는 시스템 전체의 흐름을 중심으로 테스트를 진행합니다. 두 가지 테스트 방법을 모두 사용하여 소프트웨어의 품질을 확보할 수 있습니다.

이상으로 단위 테스트와 통합 테스트의 차이점에 대해 알아보았습니다. 감사합니다.

[참고 문서](https://medium.com/@daeseungkim/단위-테스트와-통합-테스트의-차이점-319b3c2fcab2)