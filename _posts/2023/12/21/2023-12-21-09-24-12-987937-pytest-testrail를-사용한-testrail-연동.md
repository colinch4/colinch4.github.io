---
layout: post
title: "[python] pytest-testrail를 사용한 TestRail 연동"
description: " "
date: 2023-12-21
tags: [python]
comments: true
share: true
---

TestRail은 소프트웨어 테스트 계획, 추적 및 관리를 위한 웹 기반 테스트 케이스 관리 도구입니다. 테스트 팀이 테스트 계획, 실행 및 결과를 추적할 수 있도록 해주며, 품질 관리를 위한 포괄적인 솔루션을 제공합니다.

# pytest-testrail 라이브러리란 무엇인가요?

pytest-testrail는 pytest 테스트 프레임워크와 TestRail을 통합하는 파이썬 라이브러리입니다. 이 라이브러리를 사용하면 pytest를 통해 실행된 테스트 결과를 TestRail에 자동으로 보고할 수 있습니다.

# pytest-testrail를 사용해보자

## pytest-testrail 설치

먼저, pytest-testrail를 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```bash
pip install pytest-testrail
```

## TestRail 연동 설정

pytest-testrail를 사용하기 전에 TestRail과 연동하는 설정을 해야 합니다. 사용하려는 프로젝트의 TestRail API 키, URL 및 프로젝트 ID를 설정 파일에 저장합니다.

```ini
# pytest.ini 파일

[pytest]
testrail_url = https://your-testrail-instance.testrail.io/
testrail_user = your_testrail_email@example.com
testrail_api_token = your_testrail_api_token
testrail_project_id = your_testrail_project_id
```

## 테스트 케이스에 TestRail ID 부여

pytest 테스트 함수에 `@pytest.mark.testrail(id=XXX)` 데코레이터를 사용하여 TestRail의 테스트 케이스 ID를 지정합니다. 이렇게하면 특정 테스트 함수가 어떤 TestRail 테스트 케이스에 해당하는지를 나타낼 수 있습니다.

```python
import pytest

@pytest.mark.testrail(id=123)
def test_example():
    assert 1 + 2 == 3
```

## 테스트 실행 및 결과 보고

이제 설정이 완료되었으므로 pytest를 실행하여 테스트를 수행할 수 있습니다. 테스트가 완료되면 pytest-testrail은 자동으로 결과를 TestRail에 보고합니다.

## 마무리

pytest-testrail를 사용하면 pytest와 TestRail을 손쉽게 통합하여 테스트 결과를 효율적으로 관리할 수 있습니다. 테스트 케이스와 결과를 한 곳에서 추적하고 보고하는 데 필요한 작업량을 줄일 수 있으며, 팀 간의 협업을 강화할 수 있습니다.

# References
- [pytest-testrail GitHub 페이지](https://github.com/gasq/pytest-testrail)
- [TestRail 공식 웹사이트](https://www.gurock.com/testrail/)