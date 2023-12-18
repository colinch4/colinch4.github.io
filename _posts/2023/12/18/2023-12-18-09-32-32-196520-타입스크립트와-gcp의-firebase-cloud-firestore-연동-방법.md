---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Firebase Cloud Firestore 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP(Google Cloud Platform)의 Firebase는 백엔드를 구축 및 관리하기 위한 플랫폼으로, Cloud Firestore는 NoSQL 데이터베이스 솔루션 중 하나입니다. 이 튜토리얼에서는 TypeScript로 작성된 프로젝트에서 Firebase Cloud Firestore를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 및 서비스 계정 설정

우선, GCP 콘솔에 로그인하여 Firebase 프로젝트를 생성합니다. 그 후, 서비스 계정 키를 생성하여 프로젝트의 인증 정보를 제공받습니다.

## 2. 프로젝트 초기화 및 Firebase Admin SDK 설치

프로젝트 디렉토리에서 다음 명령어를 사용하여 Firebase Admin SDK를 설치합니다.

```bash
npm install firebase-admin
```

그리고 프로젝트를 초기화합니다.

```typescript
import * as admin from "firebase-admin";

const serviceAccount = require("path/to/serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();
```

위의 코드에서 `serviceAccountKey.json` 파일은 GCP 콘솔에서 서비스 계정 키를 생성할 때 다운로드받은 JSON 파일을 나타냅니다.

## 3. 데이터베이스 작업

이제 Firebase Cloud Firestore와의 상호 작용을 통해 데이터를 생성, 읽기, 업데이트 및 삭제할 수 있습니다.

### 데이터 읽기

```typescript
const docRef = db.collection('users').doc('user1');

docRef.get()
  .then((doc) => {
    if (doc.exists) {
      console.log("Document data:", doc.data());
    } else {
      console.log("No such document!");
    }
  })
  .catch((error) => {
    console.log("Error getting document:", error);
  });
```

### 데이터 쓰기

```typescript
const user = {
  name: "John Doe",
  email: "johndoe@example.com",
  age: 30
};

db.collection('users').doc('user1').set(user);
```

## 마치며

이제 TypeScript 프로젝트에서 Firebase Cloud Firestore를 사용하는 방법을 알아보았습니다. Firebase의 다른 기능과 결합하여 더 다양한 애플리케이션을 개발할 수 있습니다. 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/firestore)를 참조하시기 바랍니다.