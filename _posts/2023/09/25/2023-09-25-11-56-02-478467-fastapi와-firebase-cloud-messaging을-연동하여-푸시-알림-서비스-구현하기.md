---
layout: post
title: "FastAPI와 Firebase Cloud Messaging을 연동하여 푸시 알림 서비스 구현하기"
description: " "
date: 2023-09-25
tags: [FastAPI, FirebaseCloudMessaging]
comments: true
share: true
---

푸시 알림 서비스는 모바일 애플리케이션에서 중요한 역할을 수행합니다. 사용자에게 중요한 정보를 실시간으로 전달하고, 애플리케이션을 주목할 수 있게 만들어줍니다. 이번 블로그 포스트에서는 FastAPI와 Firebase Cloud Messaging (FCM)을 연동하여 푸시 알림 서비스를 구현하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 로그인하고, 새 프로젝트를 만듭니다.
2. 프로젝트 개요에서 "앱 추가"를 클릭하고, 푸시 알림을 구현할 플랫폼을 선택합니다 (Android 또는 iOS).
3. 앱에 대한 디테일한 설정을 완료한 후, Firebase 설정 파일을 다운로드합니다 (.json 파일).

## FastAPI 프로젝트 설정

1. FastAPI 프로젝트를 생성하고, 필요한 종속성을 설치합니다.
2. Firebase Admin SDK로 Firebase를 초기화하는 모듈을 작성합니다.
   ```python
   from fastapi import FastAPI
   import firebase_admin
   from firebase_admin import credentials

   app = FastAPI()

   def initialize_firebase():
       firebase_cred = credentials.Certificate("/path/to/firebase_credentials.json")
       firebase_admin.initialize_app(firebase_cred)

   app.add_event_handler("startup", initialize_firebase)
   ```

## Token 기반 사용자 인증

푸시 알림을 수신받을 사용자를 식별하기 위해 Firebase Auth를 사용하는 것이 일반적입니다. 사용자가 앱에 로그인하고 인증 토큰을 받은 후, FastAPI 서버에 해당 토큰을 보내 사용자를 인증할 수 있습니다.

1. FastAPI 라우터에 사용자 인증을 위한 데코레이터를 작성합니다.
   ```python
   from fastapi import Depends, HTTPException, status
   from firebase_admin import auth

   def authenticate_user(token: str = Depends(get_token_from_request)):
       try:
           decoded_token = auth.verify_id_token(token)
           uid = decoded_token['uid']
           # 사용자를 인증 처리
           # ...
       except (ValueError, auth.ExpiredTokenError, auth.InvalidIdTokenError):
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Invalid authentication credentials",
               headers={"WWW-Authenticate": "Bearer"},
           )
   ```

2. 토큰을 헤더에서 추출하는 `get_token_from_request()` 함수를 작성합니다.
   ```python
   from fastapi import Header

   def get_token_from_request(authorization: str = Header(...)):
       return authorization.replace("Bearer ", "")
   ```

## 푸시 알림 보내기

이제 사용자 인증 및 Firebase를 초기화하는 코드가 준비되었습니다. 푸시 알림을 보내기 위해 다음 단계를 수행합니다.

1. FastAPI 라우터에 푸시 알림 전송을 위한 엔드포인트를 작성합니다.
   ```python
   from firebase_admin import messaging

   @app.post('/send-push-notification')
   async def send_push_notification(user_token: str, text: str):
       message = messaging.Message(
           token=user_token,
           notification=messaging.Notification(
               title="새로운 메시지",
               body=text
           )
       )
       response = messaging.send(message)
       return response
   ```

2. 클라이언트 애플리케이션에서 사용자 토큰을 얻은 후, `send-push-notification` 엔드포인트로 요청을 보낼 수 있습니다.

## 마치며

이제 FastAPI와 Firebase Cloud Messaging(FCM)을 연동하여 푸시 알림 서비스를 구현하는 방법을 알아보았습니다. 사용자 인증과 FCM 설정을 통해 애플리케이션에서 중요하고 실시간으로 정보를 전달할 수 있는 푸시 알림 서비스를 구현할 수 있게 되었습니다.

[#FastAPI](https://twitter.com/hashtag/FastAPI) [#FirebaseCloudMessaging](https://twitter.com/hashtag/FirebaseCloudMessaging)