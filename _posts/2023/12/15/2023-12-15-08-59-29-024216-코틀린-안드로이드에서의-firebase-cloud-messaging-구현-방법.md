---
layout: post
title: "[kotlin] 코틀린 안드로이드에서의 Firebase Cloud Messaging 구현 방법"
description: " "
date: 2023-12-15
tags: [kotlin]
comments: true
share: true
---

Firebase Cloud Messaging(FCM)은 안드로이드 앱으로 푸시 알림을 보내는 데 사용되는 강력하고 유연한 도구입니다. 코틀린으로 개발한 안드로이드 앱에서 FCM을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 프로젝트를 생성하고 FCM을 설정해야 합니다. 그 후 안드로이드 앱을 Firebase 프로젝트에 연결하고 구성 파일을 다운로드하여 프로젝트에 추가합니다.

## FCM 종속성 추가

앱 수준의 build.gradle 파일에 FCM 종속성을 추가합니다.

```gradle
implementation 'com.google.firebase:firebase-messaging-ktx:22.0.0'
```

## FCM 서비스 생성

다음으로, FCM 메시지를 수신하기 위한 FCM 서비스를 만들어야 합니다. 이를 위해 FirebaseMessagingService를 확장한 새로운 클래스를 생성합니다.

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // 푸시 알림 수신 시 처리할 작업을 이곳에 구현합니다.
        // remoteMessage.getNotification()으로 메시지의 내용을 가져올 수 있습니다.
    }

    override fun onNewToken(token: String) {
        // 앱이 재설치되거나 앱 데이터가 삭제된 후에도 유효한 FCM 토큰이 생성되면 이 콜백이 호출됩니다.
        // 이 경우에 일반적으로 서버에 새 토큰을 업데이트하는 작업을 수행합니다.
    }
}
```

## AndroidManifest.xml 설정

AndroidManifest.xml에 FCM 서비스 및 사용 권한을 추가합니다.

```xml
<service
    android:name=".MyFirebaseMessagingService">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

## 푸시 알림 테스트

이제 FCM을 사용하여 푸시 알림을 안드로이드 앱으로 보낼 수 있습니다. Firebase 콘솔에서 푸시 알림을 보내거나 Firebase Admin SDK를 사용하여 서버 측에서 알림을 보낼 수 있습니다.

이상으로, 코틀린으로 안드로이드 앱에 Firebase Cloud Messaging을 구현하는 방법에 대해 알아보았습니다. Firebase의 문서 및 지원 자료를 참고하여 더 많은 기능을 구현할 수 있습니다.

더 많은 정보는 [Firebase 문서](https://firebase.google.com/docs/cloud-messaging)에서 확인할 수 있습니다.