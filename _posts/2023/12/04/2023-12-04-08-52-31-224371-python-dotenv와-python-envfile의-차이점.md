---
layout: post
title: "[python] python-dotenv와 python-envfile의 차이점"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

환경 변수를 쉽게 관리할 수 있는 Python 패키지로는 `python-dotenv`와 `python-envfile`이 있습니다. 이들 두 패키지는 환경 변수를 파일로 관리하고 로드하는 데 도움을 줍니다. 하지만 두 패키지 간에는 몇 가지 차이점이 있습니다.

## `python-dotenv`

`python-dotenv`는 `.env` 파일을 사용하여 환경 변수를 관리하는 데 사용됩니다. `.env` 파일은 키-값 쌍으로 구성된 텍스트 파일이며, 각 키-값 쌍은 한 줄에 하나씩 작성됩니다. `.env` 파일에 정의된 환경 변수는 `os.environ`을 통해 액세스할 수 있습니다.

`python-dotenv`의 장점:
- 간단하고 직관적인 구문을 사용하여 `.env` 파일을 작성할 수 있습니다.
- `.env` 파일을 프로젝트 디렉토리에 저장하여 소스 코드와 함께 버전 관리할 수 있습니다.
- `.env` 파일을 읽어와서 환경 변수를 설정하기 위해 별도의 코드가 필요하지 않습니다.

`python-dotenv`의 예시 코드:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일로부터 환경 변수 로드

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# 환경 변수 사용
print(f"Database Host: {DB_HOST}")
print(f"Database User: {DB_USER}")
print(f"Database Password: {DB_PASSWORD}")
```

## `python-envfile`

`python-envfile`은 `.env` 파일 외에도 여러 개의 파일을 사용하여 환경 변수를 관리하는 데 사용됩니다. `.env` 파일과 유사한 구문을 사용하며, 각 파일은 키-값 쌍으로 구성됩니다. `python-envfile`은 `.env` 파일이나 다른 파일에서 환경 변수를 로드하여 `os.environ`에 설정합니다.

`python-envfile`의 장점:
- 여러 개의 파일을 사용하여 환경 변수를 구성할 수 있습니다. 예를 들어, `.env.dev`, `.env.test`, `.env.prod`와 같이 다른 환경에 따라 파일을 분리하여 사용할 수 있습니다.
- `.env` 파일 이외의 다른 파일을 사용하여 환경 변수를 관리할 수 있습니다.

`python-envfile`의 예시 코드:

```python
from envfile import EnvFile
import os

env = EnvFile()
env.read(".env")  # .env 파일로부터 환경 변수 로드

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# 환경 변수 사용
print(f"Database Host: {DB_HOST}")
print(f"Database User: {DB_USER}")
print(f"Database Password: {DB_PASSWORD}")
```

## 결론

`python-dotenv`와 `python-envfile`은 모두 Python 환경 변수를 관리하는 좋은 도구입니다. 선택하는 패키지는 프로젝트의 요구 사항과 개인적인 선호도에 따라 다를 수 있습니다. 간단한 `.env` 파일만으로 환경 변수를 관리하고자 한다면 `python-dotenv`를 사용하는 것이 좋습니다. 그러나 여러 개의 파일을 사용하여 환경 변수를 관리하고 싶다면 `python-envfile`을 고려해 보세요.

---

참고 문헌:
- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
- [python-envfile Documentation](https://github.com/joho/7envfile)