---
layout: post
title: "[python] python-dotenv를 사용하여 AWS Lambda 함수 설정 관리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

AWS Lambda는 서버리스 아키텍처를 구축할 때 매우 유용한 서비스입니다. 그러나 Lambda 함수의 설정 값들을 관리하기 위해서는 일일이 환경 변수를 설정해야 합니다. 이러한 설정 관리를 보다 효과적으로 하기 위해 `python-dotenv`라이브러리를 사용할 수 있습니다.

`python-dotenv`는 `.env` 파일을 사용하여 환경 변수를 설정하는 것을 도와줍니다. 이렇게 하면 코드에서 변수를 하드코딩하는 대신 `.env` 파일에 정의된 변수를 사용할 수 있습니다.

## `python-dotenv` 설치하기

먼저, `python-dotenv`를 설치해야 합니다. 다음 명령어를 사용하여 설치할 수 있습니다.

```bash
pip install python-dotenv
```

## `.env` 파일 생성하기

`.env` 파일은 Lambda 함수 설정에 사용될 환경 변수를 포함하는 텍스트 파일입니다. 프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음과 같이 환경 변수를 정의해보세요.

```plaintext
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
AWS_REGION=us-west-2
```

## Lambda 함수에서 `python-dotenv` 사용하기

이제, Lambda 함수 코드에서 `python-dotenv`를 사용하여 `.env` 파일에 정의된 환경 변수를 불러와 사용할 수 있습니다. 예를 들어, 다음과 같이 `boto3`를 사용하여 S3 버킷에 파일을 업로드하는 코드를 작성해보겠습니다.

```python
import boto3
from dotenv import load_dotenv

# `.env` 파일 로드하기
load_dotenv()

def upload_file_to_s3(file_path, bucket_name, object_name):
    # 환경 변수 불러오기
    access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region = os.getenv("AWS_REGION")

    # S3 클라이언트 생성하기
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region
    )

    # 파일 업로드하기
    s3_client.upload_file(file_path, bucket_name, object_name)

# 사용 예시
upload_file_to_s3('image.png', 'my-s3-bucket', 'uploads/image.png')
```

위 코드에서 `load_dotenv()` 함수를 호출하여 `.env` 파일을 불러왔습니다. 그리고 환경 변수는 `os.getenv()` 함수를 사용하여 가져올 수 있습니다.

이제 Lambda 함수에서 환경 변수를 직접 하드코딩하는 대신 `.env` 파일을 통해 값을 가져와 사용할 수 있습니다. 이를 통해 환경 변수 관리가 더욱 효율적이고 유지보수가 용이해집니다.

---

## 참고 자료

- [python-dotenv GitHub 저장소](https://github.com/theskumar/python-dotenv)