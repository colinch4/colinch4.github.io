---
layout: post
title: "[python] python-dotenv와 python-decouple의 차이점"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

파이썬 프로젝트에서 환경 변수를 관리하기 위해 `python-dotenv`와 `python-decouple` 라이브러리를 사용할 수 있습니다. 이 두 라이브러리는 비슷한 목적을 가지고 있지만, 몇 가지 중요한 차이점이 있습니다.

## 1. `python-dotenv`

`python-dotenv`는 프로젝트 루트 디렉토리에 `.env` 파일을 생성하고, 환경 변수를 파일에 저장하는 방식으로 동작합니다. 

### 사용법

1. `pip install python-dotenv` 명령을 통해 패키지를 설치합니다.
2. `.env` 파일에 환경 변수를 설정합니다. 예: `DB_HOST=localhost`
3. 파이썬 코드에서 `python-dotenv`를 import하고, `load_dotenv()` 함수를 호출하여 `.env` 파일을 로드합니다. 이후 `os.getenv()`를 통해 변수를 사용할 수 있습니다.

### 장점

- `.env` 파일을 통해 환경 변수를 관리하기 때문에, 프로젝트의 다른 설정 파일과 별도로 관리할 수 있습니다.
- `.env` 파일은 인자 값과 함께 버전 제어 시스템에 추가할 수 있습니다.

### 단점

- `.env` 파일은 따로 관리해야 하기 때문에, 파일이 누락될 가능성이 있습니다.
- `.env` 파일에 저장된 환경 변수는 문자열로 저장되기 때문에 타입 변환이 필요할 수 있습니다.

## 2. `python-decouple`

`python-decouple`은 `.env` 파일 외에도 `.ini` 파일, 파이썬 클래스 등 다양한 소스에서 환경 변수를 관리할 수 있는 옵션을 제공합니다.

### 사용법

1. `pip install python-decouple` 명령을 통해 패키지를 설치합니다.
2. 설정 파일(예: `.env`, `.ini`, `.cfg` 등)에 환경 변수를 설정합니다.
3. 파이썬 코드에서 `python-decouple`를 import하고, `config()` 함수를 호출하여 설정 파일을 로드합니다. 이후 `config()`를 통해 변수를 사용할 수 있습니다.

### 장점

- 다양한 설정 파일 형식을 지원하기 때문에 사용자의 요구에 맞게 설정할 수 있습니다.
- 소스 코드에서 특정 값만 변경하는 것이 가능합니다. (ex: `.env` 파일 없이 바로 변수를 설정하는 경우)

### 단점

- `.env` 파일만을 사용하는 `python-dotenv`에 비해 설정 파일이 복잡해질 가능성이 있습니다.
- 설정 파일 형식을 변경하는 경우 코드를 수정해야 할 수도 있습니다.

## 결론

이렇게 `python-dotenv`와 `python-decouple`의 차이점을 살펴보았습니다. 두 라이브러리는 환경 변수 관리를 위한 좋은 도구입니다. 프로젝트의 요구사항에 맞게 적절한 방식을 선택하여 사용하시면 됩니다.

### 참고자료

- `python-dotenv` 공식 문서: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)
- `python-decouple` 공식 문서: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)