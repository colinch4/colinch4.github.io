---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 푸시 알림 설정하기"
description: " "
date: 2023-11-06
tags: [pushnotification, javascript]
comments: true
share: true
---

웹 또는 모바일 애플리케이션을 개발하고 있다면, 사용자에게 푸시 알림을 보내는 기능을 구현해야 할 수도 있습니다. JavaScript 프로젝트의 푸시 알림을 설정하는 방법에 대해 알아보겠습니다.

## Firebase 사용하기

Firebase는 Google에서 제공하는 백엔드 서비스 플랫폼으로, 푸시 알림을 손쉽게 구현할 수 있도록 도와줍니다. Firebase의 Cloud Messaging(FCM) 서비스를 사용하여 푸시 알림을 설정할 수 있습니다.

1. Firebase 프로젝트 생성하기
   - [Firebase 콘솔](https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성합니다.
   - 프로젝트 이름을 지정하고, 필요한 설정을 완료합니다.

2. Firebase SDK 설치하기
   - 프로젝트 루트 디렉토리에서 터미널을 열고, 다음 명령을 실행하여 Firebase SDK를 설치합니다:

     ```
     npm install firebase
     ```

3. Firebase 설정 파일 추가하기
   - Firebase 콘솔의 프로젝트 설정 페이지로 이동합니다.
   - 웹 애플리케이션을 추가하고, 제공되는 구성 파일을 다운로드합니다.
   - 다운로드한 파일을 프로젝트 루트 디렉토리에 추가합니다.

4. Firebase 초기화하기
   - JavaScript 파일에서 Firebase를 초기화합니다. 예를 들어, 다음과 같이 코드를 추가할 수 있습니다:

     ```javascript
     import firebase from "firebase/app";
     import "firebase/messaging";

     const firebaseConfig = {
       // Firebase 구성 정보 입력
     };

     firebase.initializeApp(firebaseConfig);
     ```

5. 푸시 알림 수신 허용 요청하기
   - 알림을 수신할 사용자에게 허용을 요청해야 합니다. 이를 위해 다음 코드를 사용할 수 있습니다:

     ```javascript
     const messaging = firebase.messaging();

     messaging.requestPermission().then(() => {
       console.log("알림 수신 허용됨");
     }).catch((error) => {
       console.log("알림 수신 허용 거부됨", error);
     });
     ```

6. 푸시 알림 보내기
   - 푸시 알림을 보내기 위해서는 FCM 서버에 요청을 보내야 합니다. 이를 위해 다음 코드를 사용할 수 있습니다:

     ```javascript
     const messaging = firebase.messaging();

     messaging.getToken().then((token) => {
       // 토큰 받아오기 성공 시, 푸시 알림을 FCM 서버로 전송
     }).catch((error) => {
       console.log("토큰 받아오기 실패", error);
     });
     ```

이제 JavaScript 프로젝트에서 푸시 알림을 설정할 준비가 되었습니다. Firebase의 다양한 기능을 활용하여 푸시 알림을 더욱 효과적으로 구현할 수 있습니다.

> 참고: [Firebase 공식 문서](https://firebase.google.com/docs/cloud-messaging)를 참조하면 더 자세한 내용을 확인할 수 있습니다.

#pushnotification #javascript