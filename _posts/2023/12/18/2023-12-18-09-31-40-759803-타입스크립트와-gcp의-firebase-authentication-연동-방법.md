---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Firebase Authentication 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP(Google Cloud Platform)의 Firebase Authentication을 사용하면 애플리케이션에 사용자 인증 및 관리 기능을 쉽게 추가할 수 있습니다. 이 기능을 타입스크립트 애플리케이션에 통합하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 생성
우선 GCP 콘솔에서 새로운 Firebase 프로젝트를 생성합니다. Firebase 프로젝트를 설정하고 Firebase Authentication 기능을 활성화합니다.

## 2. Firebase Admin SDK 설치
이어서, Firebase Admin SDK를 사용해 타입스크립트 애플리케이션을 Firebase 프로젝트에 연결합니다. npm을 사용하여 `firebase-admin` 패키지를 설치합니다.

```bash
npm install firebase-admin
```

## 3. 서비스 계정 키 생성
GCP 콘솔에서 서비스 계정 키를 생성하여 다운로드합니다. 이 키를 사용하여 타입스크립트 애플리케이션에서 Firebase Admin SDK에 인증합니다.

## 4. 타입스크립트 앱에 Firebase Admin SDK 통합
타입스크립트 애플리케이션에서 Firebase Admin SDK를 초기화하고 서비스 계정 키를 사용하여 연결합니다. 예를 들어, 다음과 같이 초기화할 수 있습니다.

```typescript
import * as admin from 'firebase-admin';

const serviceAccount = require('path/to/serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://your-project-id.firebaseio.com"
});
```

## 5. 인증 및 사용자 관리
이제 타입스크립트 애플리케이션에서 Firebase Authentication을 사용하여 사용자를 인증하고 관리할 수 있습니다. 예를 들어, 사용자를 생성하고 이메일/비밀번호로 인증하는 코드는 다음과 같습니다.

```typescript
admin.auth().createUser({
  email: 'user@example.com',
  emailVerified: false,
  password: 'password',
  displayName: 'John Doe',
  disabled: false,
})
  .then((userRecord) => {
    console.log('Successfully created new user:', userRecord.uid);
  })
  .catch((error) => {
    console.log('Error creating new user:', error);
  });
```

## 마무리
이제 타입스크립트 애플리케이션에서 GCP의 Firebase Authentication을 통합하는 방법에 대해 알아보았습니다. Firebase를 사용하여 인증 및 사용자 관리를 구현할 수 있는 강력한 기능을 활용하여 안전하고 효율적인 애플리케이션을 개발할 수 있습니다.

많은 도움을 주신 [Firebase 공식 문서](https://firebase.google.com/docs/admin/setup)를 참고해 주세요.