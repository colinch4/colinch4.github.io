---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Firebase Cloud Messaging 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP(Google Cloud Platform)의 Firebase Cloud Messaging(FCM)은 모바일 애플리케이션을 위한 메시지 전송을 지원하는 기능입니다. 이 기능을 타입스크립트 애플리케이션에 연동하는 방법을 살펴보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase Console에서 새 프로젝트를 생성하고, 해당 프로젝트에 FCM을 활성화합니다. 그런 다음, 애플리케이션의 키(서비스 계정 키)를 생성하여 다운로드합니다.

## 2. 타입스크립트 패키지 설치

FCM을 사용하기 위해 `firebase-admin` 패키지를 설치합니다. 이 패키지는 TypeScript와 함께 사용될 수 있습니다.

```typescript
npm install firebase-admin
```

## 3. 서비스 계정 키 설정

다운로드한 서비스 계정 키(JSON 파일)을 프로젝트 디렉터리에 추가합니다. 이 파일은 FCM을 사용하여 메시지를 보낼 때 사용됩니다.

## 4. 타입스크립트 코드 작성

이제 타입스크립트 코드에서 FCM 기능을 사용할 수 있습니다. 다음은 간단한 예시입니다.

```typescript
import * as admin from 'firebase-admin';

const serviceAccount = require('path/to/serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const message = {
  notification: {
    title: 'New Message',
    body: 'You have a new message!'
  },
  token: 'device_token'
};

admin.messaging().send(message)
  .then((response) => {
    console.log('Successfully sent message:', response);
  })
  .catch((error) => {
    console.log('Error sending message:', error);
  });
```

위 코드에서 `serviceAccountKey.json`은 다운로드한 서비스 계정 키 파일의 경로를 나타냅니다. 또한 `token`은 메시지를 받을 기기의 FCM 토큰입니다.

## 5. 애플리케이션 실행 및 테스트

위의 코드를 포함한 타입스크립트 애플리케이션을 실행하고, FCM으로 메시지를 성공적으로 전송하는지 확인합니다.

이제 타입스크립트 애플리케이션과 GCP의 Firebase Cloud Messaging이 성공적으로 연동된 것을 확인할 수 있습니다. 만약 어떤 이슈가 발생한다면, [Firebase 문서](https://firebase.google.com/docs/cloud-messaging)를 참고하시기 바랍니다.