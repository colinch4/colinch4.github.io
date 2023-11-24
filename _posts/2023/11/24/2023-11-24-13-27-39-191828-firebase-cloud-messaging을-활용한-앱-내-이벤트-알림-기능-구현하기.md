---
layout: post
title: "[swift] Firebase Cloud Messaging을 활용한 앱 내 이벤트 알림 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 사용자에게 이벤트 알림을 보내기 위해 Firebase Cloud Messaging (FCM)을 사용할 수 있습니다. FCM은 휴대폰이나 태블릿과 같은 모바일 기기로 알림을 전송하는 강력한 도구입니다. 이번 블로그 포스트에서는 Swift와 FCM을 사용하여 앱 내 이벤트 알림 기능을 구현하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정하기

Firebase를 사용하려면 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 만들고, iOS 앱용으로 프로젝트를 설정하세요. Firebase 콘솔에서 제공하는 구성 파일을 다운로드하여 Xcode 프로젝트에 추가하세요.

## 2. Firebase SDK 설치하기

Firebase SDK를 사용하여 앱에 FCM을 추가해야 합니다. CocoaPods를 사용한다면 `Podfile`에 다음과 같이 Firebase Messaging 팟을 추가하세요:

```swift
pod 'Firebase/Messaging'
```

그리고 터미널에서 다음 명령어를 실행하여 팟을 설치하세요:

```
$ pod install
```

CocoaPods를 사용하지 않는다면, Firebase Messaging SDK를 직접 다운로드하여 Xcode 프로젝트에 추가하세요.

## 3. 알림 권한 요청하기

앱을 시작할 때 알림 권한을 요청해야 합니다. `AppDelegate.swift` 파일에서 다음 코드를 추가하세요:

```swift
import UserNotifications

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // ...
    let center = UNUserNotificationCenter.current()
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
        if granted {
            application.registerForRemoteNotifications()
        }
    }
    // ...
    return true
}
```

## 4. FCM 토큰 가져오기

FCM 메시지를 보내려면 앱이 사용자 기기의 FCM 토큰을 가져와야 합니다. `AppDelegate.swift` 파일에서 다음 코드를 추가하세요:

```swift
import FirebaseMessaging

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Messaging.messaging().apnsToken = deviceToken
    // FCM 토큰 가져오기
    Messaging.messaging().token { token, error in
        if let token = token {
            // 토큰 사용
            print("FCM 토큰: \(token)")
        }
    }
}
```

## 5. 이벤트 알림 보내기

이제 FCM 토큰을 사용하여 이벤트 알림을 보낼 수 있습니다. Firebase 콘솔에서 FCM 탭을 열고 "새 알림" 버튼을 클릭하세요. 여기에서 알림의 제목, 내용 및 대상에 대한 정보를 입력할 수 있습니다. 알림을 전송하면 해당 푸시 메시지를 수신하는 앱에 알림이 표시됩니다.

```swift
import FirebaseMessaging

func sendEventNotification(title: String, body: String, token: String) {
    let message = [
        "to": token,
        "notification": [
            "title": title,
            "body": body
        ]
    ]

    // FCM 서버로 알림 전송
    Messaging.messaging().sendMessage(message, completion: { error in
        if let error = error {
            print("알림 전송 실패: \(error)")
        } else {
            print("알림 전송 성공")
        }
    })
}
```

위 코드에서 `sendEventNotification` 함수를 호출하여 이벤트 알림을 보낼 수 있습니다. 알림의 제목, 내용 및 대상 토큰을 인자로 전달하면 해당 알림이 송신됩니다.

이제 Firebase Cloud Messaging을 활용하여 앱 내 이벤트 알림 기능을 구현하는 방법을 알게 되었습니다. FCM은 사용자에게 중요한 정보를 전달하고 앱 사용자 경험을 향상시키는 강력한 도구입니다.

더 자세한 내용은 [Firebase Cloud Messaging 문서](https://firebase.google.com/docs/cloud-messaging)를 참고하세요.