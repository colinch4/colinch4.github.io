---
layout: post
title: "[python] python-dotenv를 사용하여 Kubernetes 환경 설정하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Kubernetes는 대규모 분산 시스템을 운영하기 위한 오픈소스 플랫폼으로, 환경 변수를 사용해 애플리케이션의 구성을 관리하는 것이 일반적입니다. 하지만 Kubernetes 환경에서 환경 변수를 설정하는 것은 번거로운 일일 수 있습니다. 이 문제를 해결하기 위해 python-dotenv를 사용하여 Kubernetes 환경 설정을 간편하게 할 수 있습니다.

## python-dotenv란?

python-dotenv는 Python 프로젝트에서 환경 변수를 사용하기 위한 패키지입니다. `.env` 파일에 환경 변수를 정의하고, 이를 프로젝트에서 간편하게 사용할 수 있도록 도와줍니다. 이 패키지를 사용하면 환경 변수 관리를 더욱 편하게 할 수 있습니다.

## python-dotenv 설치하기

python-dotenv를 사용하기 위해서는 먼저 패키지를 설치해야 합니다. 다음 명령어로 설치할 수 있습니다.

```shell
pip install python-dotenv
```

## Kubernetes 환경 설정하기

1. 먼저 `.env` 파일을 프로젝트 루트 디렉토리에 생성합니다.
2. `.env` 파일에 환경 변수를 정의합니다. 예를 들어, `DATABASE_URL=postgres://user:password@host:port/db`와 같이 설정할 수 있습니다.
3. Python 코드에서 `python-dotenv`를 import하고 `load_dotenv()` 함수를 호출하여 `.env` 파일을 로드합니다.
    ```python
    from dotenv import load_dotenv

    load_dotenv()
    ```
4. 이제 `os.getenv()` 함수를 사용하여 환경 변수를 읽을 수 있습니다.
    ```python
    import os

    database_url = os.getenv("DATABASE_URL")
    ```

python-dotenv를 사용하여 Kubernetes 환경 설정을 간편하게 할 수 있습니다. 이를 통해 애플리케이션을 Kubernetes에서 실행할 때 매번 환경 변수를 별도로 설정하는 번거로움을 줄일 수 있습니다.

## 참고 자료

- [python-dotenv 공식 문서](https://pypi.org/project/python-dotenv/)
- [Kubernetes 공식 문서](https://kubernetes.io/)