---
layout: post
title: "[swift] Firebase Cloud Messaging을 활용한 앱 내 이벤트 소식 전달 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging (FCM)은 모바일 앱에 대한 실시간 메시징을 쉽게 구현할 수 있는 플랫폼입니다. 이번 기사에서는 Swift로 개발된 iOS 앱에서 FCM을 사용하여 앱 내 이벤트 소식을 전달하는 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

가장 먼저 해야 할 일은 Firebase 프로젝트를 설정하는 것입니다.

1. Firebase 콘솔에 로그인하고, 새 프로젝트를 생성합니다.
2. 앱을 iOS로 추가합니다. 앱 번들 식별자와 앱 닉네임을 입력합니다.
3. GoogleService-Info.plist 파일을 다운로드하고, 프로젝트에 추가합니다.

## 2. FCM 설정

Firebase 프로젝트 설정이 완료되면, FCM 설정을 해야 합니다.

1. 앱에 Firebase SDK를 설치합니다. `AppDelegate.swift` 파일을 열고, `didFinishLaunchingWithOptions` 메소드에서 `FirebaseApp.configure()`를 호출합니다.
2. `AppDelegate.swift` 파일에 다음과 같은 코드를 추가하여 FCM 토큰을 받아올 수 있도록 설정합니다.

```swift
import FirebaseMessaging

...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    registerForPushNotifications()
    return true
}

func registerForPushNotifications() {
    UNUserNotificationCenter.current().delegate = self
    Messaging.messaging().delegate = self
    
    UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .badge, .sound]) { granted, error in
        if granted {
            DispatchQueue.main.async {
                UIApplication.shared.registerForRemoteNotifications()
            }
        }
    }
    
    Messaging.messaging().token { token, error in
        if let token = token {
            // FCM 토큰을 가져왔을 때의 동작을 구현합니다.
        }
    }
}
```

3. 앱이 백그라운드 상태에서도 푸시 알림을 수신할 수 있도록 설정하기 위해 `AppDelegate.swift` 파일에 다음과 같은 코드를 추가합니다.

```swift
import UserNotifications

...

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    let userInfo = response.notification.request.content.userInfo
    
    // 푸시 알림을 클릭했을 때의 동작을 구현합니다.
    
    completionHandler()
  }
}

extension AppDelegate: MessagingDelegate {
    func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
        // FCM 토큰을 업데이트할 때의 동작을 구현합니다.
    }
}
```

## 3. 서버에서 FCM 메시지 보내기

서버에서 FCM 메시지를 보내기 위해 백엔드 개발자와 협업하여 필요한 API를 구현해야 합니다. Firebase에서 제공하는 Admin SDK를 사용하여 서버 앱에 FCM 기능을 추가할 수 있습니다.

서버에서 FCM 메시지를 보내는 방법은 Firebase 공식 문서를 참조하시기 바랍니다.

## 4. 앱에서 FCM 메시지 처리하기

앱이 푸시 알림을 수신하고 FCM 메시지를 처리하려면, `AppDelegate.swift` 파일에 다음과 같은 코드를 추가합니다.

```swift
import FirebaseMessaging

...

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    let userInfo = response.notification.request.content.userInfo
    
    // FCM 메시지를 처리하는 로직을 구현합니다.
    
    completionHandler()
  }
}

extension AppDelegate: MessagingDelegate {
    func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
        // FCM 토큰을 업데이트할 때의 동작을 구현합니다.
    }
}
```

`didReceive` 메소드에서 FCM 메시지를 받았을 때의 동작을 구현합니다. 앱에서 필요한 작업을 수행하거나 알림을 표시하는 등의 로직을 추가합니다.

## 결론

여기서는 Firebase Cloud Messaging을 활용하여 Swift로 개발된 iOS 앱에서 앱 내 이벤트 소식을 전달하는 기능을 구현하는 방법을 살펴보았습니다. Firebase의 강력한 기능을 활용하여 사용자에게 실시간으로 정보를 전달할 수 있습니다. Firebase 공식 문서와 관련 자료들을 참고하여 FCM을 더욱 효과적으로 활용해 보시기 바랍니다.

## 참고 자료

- [Firebase 공식 문서](https://firebase.google.com/docs/cloud-messaging)
- [Firebase Cloud Messaging iOS 클라이언트 라이브러리](https://firebase.google.com/docs/cloud-messaging/ios/client)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)