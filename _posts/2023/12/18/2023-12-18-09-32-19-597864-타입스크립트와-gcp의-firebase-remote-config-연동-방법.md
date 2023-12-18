---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Firebase Remote Config 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

본 포스트에서는 타입스크립트 프로젝트에서 Google Cloud Platform(GCP)의 Firebase Remote Config를 연동하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

우선, GCP 콘솔에서 Firebase 프로젝트를 생성하고 Firebase Remote Config를 활성화합니다. Firebase 콘솔에서 프로젝트의 웹 앱을 설정하고, Firebase SDK를 프로젝트에 추가합니다.

## 2. 타입스크립트 프로젝트 구성

타입스크립트 프로젝트를 생성하고, Firebase 모듈을 설치합니다.

```typescript
npm install firebase @types/firebase
```

Firebase 모듈을 초기화하고 Remote Config를 가져옵니다.

```typescript
import * as firebase from 'firebase/app';
import 'firebase/remote-config';

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);
const remoteConfig = firebase.remoteConfig();
```

## 3. Remote Config 사용

Remote Config를 사용하여 앱에 필요한 구성 값을 가져옵니다.

```typescript
remoteConfig.fetchAndActivate()
  .then(() => {
    const value = remoteConfig.getValue('your_config_key').asString();
    console.log('Config value:', value);
  })
  .catch((error) => {
    console.error('Error fetching remote config:', error);
  });
```

위 코드에서 `your_config_key`에는 원하는 구성 키를 지정하여 해당하는 값을 가져오면 됩니다.

이제 타입스크립트 프로젝트에서 Firebase Remote Config를 성공적으로 사용할 수 있게 되었습니다.

위 방법을 통해 타입스크립트 프로젝트와 GCP의 Firebase Remote Config를 연동하는 방법에 대해 알아보았습니다.

더 많은 정보를 원하시거나 기술적인 내용을 확인하고 싶으시다면, [Firebase 공식 문서](https://firebase.google.com/docs/remote-config)를 참고하시기 바랍니다.