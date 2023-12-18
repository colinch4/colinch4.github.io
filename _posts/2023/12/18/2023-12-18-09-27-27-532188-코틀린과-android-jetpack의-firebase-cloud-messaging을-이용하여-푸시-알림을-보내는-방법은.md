---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 Firebase Cloud Messaging을 이용하여 푸시 알림을 보내는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

## 1. Firebase 프로젝트 설정
먼저, Firebase 콘솔에서 프로젝트를 생성하고 FCM을 활성화합니다. 프로젝트 설정에서 안드로이드 앱에 대한 구성 파일을 다운로드하고, 프로젝트의 `google-services.json` 파일을 앱 모듈 디렉토리에 추가합니다.

## 2. 안드로이드 프로젝트 설정
안드로이드 프로젝트의 `build.gradle` 파일에 Firebase 및 FCM 종속성을 추가합니다.

```gradle
// 프로젝트 수준 build.gradle
classpath 'com.google.gms:google-services:4.3.3'

// 앱 모듈 수준 build.gradle
implementation 'com.google.firebase:firebase-messaging:22.0.0'
```

그런 다음, FCM을 초기화하고 토큰을 가져오는 코드를 앱의 `MainActivity` 또는 `Application` 클래스에 추가합니다.

```kotlin
// Firebase 초기화
FirebaseApp.initializeApp(this)

// FCM 토큰 가져오기
FirebaseInstanceId.getInstance().instanceId.addOnSuccessListener { instanceIdResult ->
    val token = instanceIdResult.token
    // 토큰을 사용하여 서버에 등록 또는 업데이트를 수행
}
```

## 3. 푸시 알림 수신 설정
푸시 알림을 받기 위해 `FirebaseMessagingService`를 확장하고 `onMessageReceived` 메서드를 재정의하여 수신된 메시지를 처리합니다.

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // 수신된 푸시 알림 처리
        // remoteMessage.notification으로 푸시 알림의 내용 및 데이터에 접근 가능
    }
}
```

마지막으로, Manifest 파일에 서비스를 등록합니다.

```xml
<service android:name=".MyFirebaseMessagingService">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>
```

이제 코틀린 및 Android Jetpack을 사용하여 Firebase Cloud Messaging을 통해 푸시 알림을 성공적으로 보낼 수 있습니다.