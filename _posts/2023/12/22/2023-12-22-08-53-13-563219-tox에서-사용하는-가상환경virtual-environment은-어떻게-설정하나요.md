---
layout: post
title: "[python] tox에서 사용하는 가상환경(Virtual Environment)은 어떻게 설정하나요?"
description: " "
date: 2023-12-22
tags: [python]
comments: true
share: true
---

```ini
[tox]
envlist = py38, py39

[testenv]
deps = pytest
commands = pytest
```

이 설정에서 `tox`는 테스트 환경을 정의하는 부분입니다. `envlist`는 실행할 환경의 리스트를 지정하고, `testenv` 섹션은 각 환경에서 필요한 의존성과 실행할 명령을 설정합니다.

`tox`를 실행하면 이 설정에 따라 가상환경이 만들어지고 테스트가 실행됩니다. 이를 통해 다양한 버전의 파이썬 및 다양한 의존성 환경에서 코드를 실행하여 테스트할 수 있습니다.

관련해서 더 알고 싶다면 [tox 공식문서](https://tox.readthedocs.io/en/latest/config.html)를 참고하세요.