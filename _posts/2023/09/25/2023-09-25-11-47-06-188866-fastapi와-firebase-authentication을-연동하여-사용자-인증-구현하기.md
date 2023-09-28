---
layout: post
title: "FastAPI와 Firebase Authentication을 연동하여 사용자 인증 구현하기"
description: " "
date: 2023-09-25
tags: [FastAPI, Firebase]
comments: true
share: true
---

Firebase Authentication은 사용자를 쉽게 인증하고 관리할 수 있는 클라우드 기반의 인증 서비스입니다. 이번에는 FastAPI와 Firebase Authentication를 연동하여 사용자 인증 기능을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 접속하여 새로운 프로젝트를 생성합니다.
2. "Authentication" 탭으로 이동하여 "로그인 및 가입" 섹션에서 "이메일/비밀번호"를 활성화합니다.
3. 왼쪽 메뉴에서 "프로젝트 설정"을 선택하고, "일반" 탭에서 "웹 앱"을 추가합니다.
4. 앱의 이름을 입력하고, "Firebase SDK 스니펫"을 선택하여 나타난 구성 정보를 확인합니다.

## FastAPI 프로젝트 설정

1. FastAPI 프로젝트를 생성하고 필요한 패키지들을 설치합니다:
   ```python
   pip install fastapi firebase-admin python-jose[cryptography]
   ```
2. Firebase Admin SDK를 초기화하고 서비스 계정 키를 설정합니다. Firebase 콘솔에서 다운로드한 `serviceAccountKey.json` 파일을 프로젝트 루트에 저장합니다.
   ```python
   import firebase_admin
   from firebase_admin import credentials

   cred = credentials.Certificate("serviceAccountKey.json")
   firebase_admin.initialize_app(cred)
   ```
3. FastAPI 엔드포인트에서 사용자 인증을 구현합니다. 예를 들어, 사용자가 로그인하고 토큰을 발급받는 엔드포인트를 구현하려면 다음과 같이 작성합니다:
   ```python
   from fastapi import FastAPI, HTTPException
   from fastapi.security import OAuth2PasswordRequestForm
   from firebase_admin import auth

   app = FastAPI()

   @app.post("/login")
   async def login(form_data: OAuth2PasswordRequestForm):
       try:
           user = auth.get_user_by_email(form_data.username)
           token = await user.id_token
           return {"access_token": token}
       except auth.AuthError as e:
           raise HTTPException(status_code=401, detail=str(e))
   ```

## 테스트 및 실행

1. FastAPI 서버를 실행합니다:
   ```python
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. 테스트를 위해 `/login` 엔드포인트로 POST 요청을 보냅니다. 요청 시 `username`에 이메일 주소와 `password`에 비밀번호를 전달합니다.
   ```bash
   curl -X POST -d "username=test@example.com&password=12345678" http://localhost:8000/login
   ```

FastAPI와 Firebase Authentication을 연동하여 사용자 인증 기능을 구현하는 방법에 대해 알아보았습니다. Firebase Authentication은 강력한 보안과 다양한 인증 방식을 제공하여 사용자 관리를 간편하게 할 수 있습니다. 이를 활용하여 안전하고 신뢰할 수 있는 웹 애플리케이션을 개발할 수 있습니다.

#FastAPI #Firebase