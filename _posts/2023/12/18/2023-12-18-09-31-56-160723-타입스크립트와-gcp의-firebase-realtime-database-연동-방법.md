---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Firebase Realtime Database 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

본 포스트에서는 타입스크립트를 사용하여 Google Cloud Platform의 Firebase Realtime Database와의 연동 방법에 대해 안내하겠습니다.

## 1. Firebase 프로젝트 설정

우선, Firebase 콘솔을 통해 새 프로젝트를 생성하고, Realtime Database를 활성화합니다. 그 후, 앱에 Firebase를 추가하고 구성 파일을 다운로드합니다.

## 2. 타입스크립트 프로젝트 설정

다음으로, 타입스크립트 프로젝트를 설정합니다. 프로젝트 디렉토리에서 Firebase 모듈을 설치합니다.

```bash
npm install firebase @types/firebase
```

## 3. Firebase 연결 및 데이터 읽기/쓰기

타입스크립트 파일에서 Firebase를 초기화하고 Realtime Database에 연결합니다. 데이터를 읽거나 쓰려면 적절한 권한이 필요하므로 Firebase 규칙을 설정하는 것이 중요합니다.

다음은 타입스크립트에서 Firebase Realtime Database를 사용하여 데이터를 읽고 쓰는 예시 코드입니다.

```typescript
import firebase from 'firebase/app';
import 'firebase/database';

// Firebase 구성 파일을 불러와서 초기화
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  databaseURL: "YOUR_DATABASE_URL",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);

// Realtime Database 참조
const database = firebase.database();

// 데이터 읽기
database.ref('path/to/data').once('value').then((snapshot) => {
  const data = snapshot.val();
  console.log(data);
});

// 데이터 쓰기
database.ref('path/to/data').set('new data');
```

## 4. 보안 규칙 구성

Firebase Realtime Database에는 데이터 베이스에 접근하는 규칙을 구성할 수 있습니다. 이를 통해 데이터의 읽기/쓰기 권한을 제어할 수 있습니다. 규칙은 Firebase 콘솔에서 설정할 수 있습니다.

이제 타입스크립트와 GCP의 Firebase Realtime Database를 연결하는 방법에 대해 알아보았습니다. 데이터베이스를 설정하고, 데이터를 읽고 쓰는 과정에서 주의해야 할 점들을 숙지하여 안전한 애플리케이션을 개발할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/database)를 참고하시기 바랍니다.