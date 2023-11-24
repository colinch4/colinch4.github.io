---
layout: post
title: "[swift] Firebase Cloud Messaging을 활용한 앱 내 이벤트 정보 전달 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요
Firebase Cloud Messaging(FCM)은 Google의 클라우드 메시징 서비스로, 앱에서 사용자에게 메시지를 전달하는 기능을 제공합니다. 이 기능을 활용하여 앱 내 이벤트 정보를 실시간으로 전달하는 기능을 구현해보겠습니다.

## 1. Firebase 프로젝트 설정
FCM을 사용하기 위해 먼저 Firebase 프로젝트를 생성하고 설정해야 합니다. Firebase 콘솔로 이동하여 새 프로젝트를 생성하고, 앱을 추가합니다. iOS 앱에 대해 설정을 진행하고, 구성 파일을 다운로드하여 프로젝트에 포함시킵니다.

## 2. Firebase SDK 설치
Firebase SDK를 사용하여 FCM을 구현하기 위해 Cocoapods를 사용하여 필요한 라이브러리를 설치합니다. 프로젝트의 Podfile에 다음과 같이 Firebase/Core와 Firebase/Messaging를 추가합니다.

```swift
pod 'Firebase/Core'
pod 'Firebase/Messaging'
```

설치가 완료되면 터미널을 열고 프로젝트 디렉토리로 이동하여 `pod install` 명령어를 실행합니다.

## 3. AppDelegate 설정
FCM을 사용하기 위해 AppDelegate 클래스에 Firebase 초기화 코드를 추가합니다. 다음과 같은 코드를 `application(_:didFinishLaunchingWithOptions:)` 메서드에 추가합니다.

```swift
import Firebase

// ...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    
    // ...
    
    return true
}
```

또한, FCM을 사용하기 위해 AppDelegate 클래스에 `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` 메서드를 추가하여 디바이스 토큰을 등록할 수 있도록 합니다.

```swift
import FirebaseMessaging

// ...

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    print("Device Token: \(token)")
    
    Messaging.messaging().apnsToken = deviceToken
}
```

## 4. FCM 등록
사용자가 앱에서 로그인 또는 회원 가입을 할 때, FCM 등록 토큰을 얻어 서버로 전송하는 작업을 수행합니다. 사용자가 로그아웃하거나 앱을 제거할 때는 등록된 토큰을 서버에서 삭제합니다. 이를 위해 적절한 위치에 다음과 같은 코드를 추가합니다.

```swift
import FirebaseMessaging

// ...

Messaging.messaging().token { token, error in
    if let error = error {
        print("Error fetching FCM registration token: \(error)")
    } else if let token = token {
        print("FCM registration token: \(token)")
        // 서버로 토큰 전송
    }
}
```

## 5. 이벤트 정보 전달
서버에서 이벤트 정보를 생성 또는 업데이트할 때, 해당 이벤트에 대한 FCM 푸시 알림을 모든 구독자에게 보내야 합니다. 이를 위해 서버에서 Firebase Admin SDK를 사용하여 FCM을 전송하는 코드를 작성하고 호출합니다. 예를 들어, 다음과 같은 함수를 작성하여 이벤트 정보를 FCM으로 전송할 수 있습니다.

```swift
import FirebaseAdmin

// ...

func sendEventNotification(toRegistrationTokens tokens: [String], title: String, body: String) {
    let message = Messaging.messaging().Message(title: title, body: body)
    let sender = Messaging.messaging().sender()
    
    sender.send(message, to: tokens) { error in
        if let error = error {
            print("Error sending FCM message: \(error)")
        } else {
            print("FCM message sent successfully")
        }
    }
}
```

위의 코드에서 `toRegistrationTokens`에는 푸시 알림을 받을 대상의 FCM 등록 토큰 배열을 전달하면 됩니다.

## 참고 자료
- Firebase Documentation: [https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging)
- Firebase Messaging API Reference: [https://firebase.google.com/docs/reference/ios/firebase/messaging](https://firebase.google.com/docs/reference/ios/firebase/messaging)
- Firebase Admin SDK: [https://firebase.google.com/docs/admin/setup](https://firebase.google.com/docs/admin/setup)