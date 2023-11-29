---
layout: post
title: "[python] Django REST framework에서의 사용자 메시지(Push Notification) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

모바일 애플리케이션을 개발할 때, 사용자에게 메시지를 전송하는 기능은 매우 중요합니다. Django REST framework는 이러한 사용자 메시지를 처리하기 위한 다양한 방법을 제공합니다.

## 1. Firebase Cloud Messaging(Firebase Cloud Messaging, FCM) 사용하기

Firebase Cloud Messaging(FCM)는 Android, iOS 및 웹 푸시 알림을 전송하기 위한 권장된 방법입니다. FCM을 사용하기 위해서는 다음 단계를 따르면 됩니다:

### 단계 1: Firebase 프로젝트 생성

Firebase 콘솔에서 새 프로젝트를 생성합니다. Firebase 설정 파일(firebase-admin-sdk.json)을 다운로드하여 Django 프로젝트의 루트 디렉토리에 저장합니다.

### 단계 2: Firebase Admin SDK 설치

Django 프로젝트의 가상 환경에서 Firebase Admin SDK를 설치합니다:

```
pip install firebase-admin
```

### 단계 3: FCM 토큰 등록

사용자가 로그인 또는 회원가입 시 FCM 토큰을 등록하도록 구현합니다. FCM 토큰은 사용자의 디바이스를 식별하는 역할을 합니다.

### 단계 4: 메시지 전송

Django 프로젝트에서 FCM 토큰을 사용하여 메시지를 전송합니다. 다음은 Django REST framework에서 FCM을 사용하여 메시지를 전송하는 예제 코드입니다:

```python
import firebase_admin
from firebase_admin import credentials, messaging

# Firebase Admin SDK 인증 정보 로드
cred = credentials.Certificate('path/to/firebase-admin-sdk.json')
firebase_admin.initialize_app(cred)

def send_push_notification(user_id, message):
    # 사용자의 FCM 토큰 조회
    fcm_token = get_fcm_token(user_id)

    # FCM 메시지 생성
    fcm_message = messaging.Message(
        data={
            'title': 'New Message',
            'message': message
        },
        token=fcm_token
    )

    # FCM 메시지 전송
    response = messaging.send(fcm_message)
    print('Successfully sent message:', response)
```

위의 코드에서 `send_push_notification` 함수는 사용자 ID와 메시지를 인자로 받아 FCM을 사용하여 메시지를 전송합니다.

## 2. 푸시 알림 서비스(OneSignal, Pusher, 등) 사용하기

Firebase 외에도 다른 푸시 알림 서비스를 사용할 수도 있습니다. OneSignal이나 Pusher와 같은 서비스는 간편하게 사용자 메시지를 처리할 수 있는 기능을 제공합니다. 각 서비스의 공식 문서를 참고하여 설정을 진행하고, 해당 서비스의 SDK를 Django 프로젝트에 통합하여 사용자 메시지를 처리할 수 있습니다.

## 결론

Django REST framework에서 사용자 메시지를 처리하는 방법에는 Firebase Cloud Messaging을 사용하거나 다른 푸시 알림 서비스를 사용하는 방법이 있습니다. 그 중에서도 Firebase Cloud Messaging은 많은 개발자들에게 권장되는 방법이며, 다른 서비스에 비해 사용하기도 간편합니다. 하지만 개발자가 자신의 상황에 맞게 적절한 방법을 선택하여 구현할 수 있습니다.

## 참고 자료

- [Firebase Cloud Messaging 문서](https://firebase.google.com/docs/cloud-messaging/)
- [Django REST framework 문서](https://www.django-rest-framework.org/)
- [OneSignal 공식 사이트](https://onesignal.com/)
- [Pusher 공식 사이트](https://pusher.com/)