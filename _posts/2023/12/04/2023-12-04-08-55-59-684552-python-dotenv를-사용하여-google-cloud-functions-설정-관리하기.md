---
layout: post
title: "[python] python-dotenv를 사용하여 Google Cloud Functions 설정 관리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Google Cloud Functions은 서버리스 컴퓨팅 서비스로, 애플리케이션의 로직을 트리거에 따라 실행할 수 있습니다. 하지만, 애플리케이션의 설정 값들을 소스 코드에 하드코딩하는 것은 보안상 좋지 않을 뿐만 아니라, 변경이 필요한 경우 다시 배포해야 하는 번거로움이 있습니다.

이 문제를 해결하기 위해 `python-dotenv` 라이브러리를 사용하여 Google Cloud Functions의 환경 변수를 관리하는 방법에 대해 알아보겠습니다.

## 1. python-dotenv 설치하기

`python-dotenv`는 파이썬 애플리케이션에서 환경 변수를 로드하는 데 사용되는 라이브러리입니다. 다음 명령을 사용하여 설치할 수 있습니다.

```python
pip install python-dotenv
```

## 2. `.env` 파일 생성하기

Google Cloud Functions에서 사용할 환경 변수 값을 저장할 `.env` 파일을 프로젝트 루트 디렉토리에 생성합니다. 이 파일에는 키-값 쌍으로 환경 변수를 정의합니다.

```
API_KEY=my-api-key
SECRET_KEY=my-secret-key
DATABASE_URL=my-database-url
```

## 3. 환경 변수 로드하기

Cloud Function의 소스 코드에서 `python-dotenv`를 사용하여 `.env` 파일에 정의된 환경 변수를 로드합니다.

```python
from dotenv import load_dotenv

def cloud_function(request):
    load_dotenv() # .env 파일 로드
    
    api_key = os.environ.get("API_KEY")
    secret_key = os.environ.get("SECRET_KEY")
    database_url = os.environ.get("DATABASE_URL")
    
    # 환경 변수를 사용하여 애플리케이션 로직 수행
    
    return "Success!"
```

위의 예제에서는 `load_dotenv` 함수를 호출하여 `.env` 파일을 로드한 후, `os.environ.get` 메서드를 사용하여 환경 변수의 값을 가져와서 사용합니다.

## 4. Google Cloud Functions에서 .env 파일 사용하기

Google Cloud Functions는 환경 변수를 직접 로드할 수 있는 기능을 지원하지 않습니다. 대신, Cloud Functions의 환경 설정을 통해 환경 변수를 설정해야합니다.

Cloud Functions 콘솔에서 트리거 설정 페이지로 이동하여 "환경 변수" 섹션에서 다음 단계에 따라 환경 변수를 설정할 수 있습니다.
1. `API_KEY`와 같은 환경 변수 이름을 "키" 필드에 입력합니다.
2. `.env` 파일에서 해당 환경 변수의 값을 복사하여 "값" 필드에 입력합니다.
3. "만들기" 버튼을 클릭하여 환경 변수를 추가합니다.

## 결론

`python-dotenv` 라이브러리를 사용하여 Google Cloud Functions의 설정 값을 `.env` 파일에 저장하고, 코드에서 환경 변수를 로드하는 방법에 대해 알아보았습니다. 이를 통해 설정 값의 보안을 강화하고, 변경이 필요한 경우에도 불필요한 배포를 하지 않아도 되는 장점이 있습니다.

더 자세한 내용은 [python-dotenv 공식 문서](https://github.com/theskumar/python-dotenv)를 확인할 수 있습니다.