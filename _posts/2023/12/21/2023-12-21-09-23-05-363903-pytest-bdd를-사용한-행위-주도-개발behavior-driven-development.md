---
layout: post
title: "[python] pytest-bdd를 사용한 행위 주도 개발(Behavior-Driven Development)"
description: " "
date: 2023-12-21
tags: [python]
comments: true
share: true
---

행위 주도 개발(Behavior-Driven Development, BDD)은 사용자의 행동을 중심으로 소프트웨어를 개발하는 방법론입니다. pytest-bdd는 Python용 BDD 프레임워크로, 사용자와 개발자 간의 의사소통을 촉진하며 더 나은 소프트웨어를 개발할 수 있도록 도와줍니다.

## pytest-bdd 라이브러리 설치

먼저, pytest-bdd 라이브러리를 설치합니다. pip를 사용하여 간단히 설치할 수 있습니다.

```bash
pip install pytest-bdd
```

## 테스트 작성하기

pytest-bdd를 사용하여 BDD 스타일로 테스트를 작성해보겠습니다.

먼저, `features` 디렉토리 안에 `.feature` 파일을 생성하여 시나리오를 정의합니다.

예를 들어, `calculator.feature` 파일을 생성하고 다음과 같은 내용을 작성합니다.

```gherkin
Feature: Calculator
    As a user
    I want to use a calculator
    So that I can perform basic arithmetic operations

    Scenario: Add two numbers
        Given the calculator is turned on
        When I enter "2+2"
        Then the result should be 4

    Scenario: Subtract two numbers
        Given the calculator is turned on
        When I enter "5-3"
        Then the result should be 2
```

그다음, 해당 시나리오에 대한 테스트 스텝을 `steps` 디렉토리 안에 정의합니다.

예를 들어, `test_calculator.py` 파일을 생성하고 다음과 같은 내용을 작성합니다.

```python
from pytest_bdd import scenarios, given, when, then

scenarios('calculator.feature')

@given('the calculator is turned on')
def calculator():
    return Calculator()

@when('I enter "<expression>"')
def enter_expression(calculator, expression):
    calculator.enter(expression)

@then('the result should be <result>')
def result(calculator, result):
    assert calculator.result == result
```

## 테스트 실행하기

테스트를 실행하려면 다음과 같이 명령을 실행합니다.

```bash
pytest
```

pytest는 `.feature` 파일과 `.py` 파일을 자동으로 인식하여 테스트를 실행하고 결과를 출력합니다.

이제, pytest-bdd를 사용하여 BDD 스타일로 Python 애플리케이션을 개발할 준비가 되었습니다.

## 결론

pytest-bdd를 사용하면 BDD 스타일로 손쉽게 테스트를 작성하고 실행할 수 있습니다. 이를 통해 사용자의 요구 사항을 더 명확하게 이해하고, 더 나은 소프트웨어를 개발할 수 있습니다.

더 많은 정보를 원하시면 공식 문서([pytest-bdd 공식 문서](https://github.com/pytest-dev/pytest-bdd))를 참고하시기 바랍니다.