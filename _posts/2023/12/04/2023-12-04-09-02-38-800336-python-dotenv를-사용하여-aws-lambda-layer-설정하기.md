---
layout: post
title: "[python] python-dotenv를 사용하여 AWS Lambda Layer 설정하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

## 서론
AWS Lambda는 서버리스 아키텍처를 구현하기 위한 플랫폼으로, 코드를 실행하기 위해 필요한 리소스를 관리해줍니다. 이 중에서도 Lambda Layer는 코드의 종속성(Dependency)을 포함한 공유 리소스를 캡슐화하여 여러 Lambda 함수에서 재사용할 수 있도록 돕는 기능입니다. 이번 블로그 포스트에서는 `python-dotenv`를 Lambda Layer로 설정하는 방법을 소개하겠습니다.

## Python-Dotenv란?
`python-dotenv`는 Python 프로젝트에서 .env 파일을 사용하여 환경 변수를 관리할 수 있는 라이브러리입니다. 주로 로컬 개발 환경에서 사용되며, .env 파일에 정의된 환경 변수들을 Python 코드에서 사용할 수 있습니다.

## AWS Lambda Layer 설정하기
다음은 AWS Lambda Layer에 `python-dotenv`를 설정하는 방법입니다.

1. `python-dotenv` 패키지를 설치합니다.

   ```bash
   $ pip install python-dotenv
   ```

2. Lambda Layer용 폴더를 생성합니다.

   ```bash
   $ mkdir python-dotenv-layer
   $ cd python-dotenv-layer
   ```

3. `python-dotenv` 패키지를 압축합니다.

   ```bash
   $ pip install -t . python-dotenv
   $ zip -r python-dotenv-layer.zip .
   ```

4. AWS Management Console에 로그인하여 [Lambda 콘솔](https://console.aws.amazon.com/lambda)로 이동합니다.

5. Layer를 생성하기 위해 **Layers** 메뉴로 이동합니다.

6. **Create Layer** 버튼을 클릭합니다.

7. Layer에 대한 정보를 입력합니다. 이때, **Compatible runtimes**에는 Lambda 함수에서 사용하는 Python 버전을 선택합니다.

8. **Upload** 버튼을 클릭하여 압축한 `python-dotenv-layer.zip` 파일을 업로드합니다.

9. **Create** 버튼을 클릭하여 Lambda Layer를 생성합니다.

10. Lambda 함수에 생성한 Layer를 추가합니다.

    - Lambda 함수 편집 화면으로 이동합니다.

    - **Layers** 섹션에서 **Add a layer** 버튼을 클릭합니다.

    - 추가할 Layer를 선택합니다.

    - 변경 사항을 저장합니다.

이제 Lambda 함수에서 `python-dotenv`를 사용할 준비가 되었습니다. `.env` 파일에 정의된 환경 변수는 Lambda 함수에서 접근할 수 있습니다.

## 결론
이번 포스트에서는 `python-dotenv`를 AWS Lambda Layer로 설정하는 방법에 대해 알아보았습니다. `python-dotenv`를 사용하면 로컬 환경에서 환경 변수를 쉽게 관리할 수 있으며, 이를 Lambda 함수에서도 활용할 수 있습니다. Lambda Layer를 활용하여 코드의 종속성을 캡슐화함으로써 코드의 재사용성과 유지보수성을 높일 수 있습니다.