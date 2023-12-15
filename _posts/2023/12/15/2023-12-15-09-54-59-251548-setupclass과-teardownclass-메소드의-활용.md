---
layout: post
title: "[python] setUpClass()과 tearDownClass() 메소드의 활용"
description: " "
date: 2023-12-15
tags: [python]
comments: true
share: true
---

Python의 `unittest` 모듈은 유닛 테스트를 위한 다양한 기능을 제공합니다. 이 중에서 `setUpClass()`와 `tearDownClass()` 메소드는 클래스 전체에 걸쳐 한 번씩 실행되는 테스트 설정과 정리 기능을 제공합니다. 이러한 메소드들은 클래스 레벨에서 실행되기 때문에 테스트 동안에 필요한 전역적인 설정 및 정리 작업을 위해 사용됩니다.

## setUpClass() 메소드

`setUpClass()` 메소드는 테스트 클래스가 시작될 때 한 번 호출되며, 해당 클래스의 모든 테스트 메소드 실행 전에 특정한 설정을 수행합니다. 예를 들어, 데이터베이스 연결, 파일 로딩, 네트워크 연결 등의 전역적인 설정 작업을 `setUpClass()` 내에서 수행할 수 있습니다. 이렇게 함으로써 테스트 메소드들이 실행되기 전에 필요한 환경이 설정됩니다.

아래는 `setUpClass()` 메소드를 사용한 예시입니다.

```python
import unittest

class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass - This method is called once at the beginning of the test class')

    def test_add(self):
        result = 10 + 5
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = 10 - 5
        self.assertEqual(result, 5)
```

## tearDownClass() 메소드

`tearDownClass()` 메소드는 테스트 클래스가 끝날 때 한 번 호출되며, `setUpClass()` 메소드에서 설정한 환경을 정리합니다. 데이터베이스 연결을 종료하거나 파일을 닫는 등의 정리 작업을 `tearDownClass()` 내에서 수행할 수 있습니다. 이렇게 함으로써 테스트 클래스 실행 후에 사용한 자원들을 정리하여 메모리 누수 등을 방지할 수 있습니다.

아래는 `tearDownClass()` 메소드를 사용한 예시입니다.

```python
import unittest

class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass - This method is called once at the beginning of the test class')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass - This method is called once at the end of the test class')
```

`setUpClass()`와 `tearDownClass()` 메소드를 통해 유닛 테스트 클래스 수준에서의 설정 및 정리 작업을 효율적으로 관리할 수 있습니다.

위의 예시 코드를 참고하면서 `setUpClass()`과 `tearDownClass()` 메소드를 적절히 활용하여 테스트 클래스의 설정과 정리를 보다 효율적으로 관리할 수 있습니다.

## 참고 자료
- [Python unittest - Official Documentation](https://docs.python.org/3/library/unittest.html)