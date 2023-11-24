---
layout: post
title: "[swift] Firebase Cloud Messaging을 통한 푸시 알림 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging (FCM)은 개발자들이 안드로이드, iOS 및 웹 응용 프로그램으로 푸시 알림을 보낼 수 있는 강력한 도구입니다. 이 글에서는 Firebase를 사용하여 iOS 앱에 FCM을 통해 푸시 알림을 구현하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

1. Firebase 콘솔에 접속하여 프로젝트를 생성합니다.
2. iOS 앱을 추가하고, Bundle Identifier를 입력합니다.
3. `GoogleService-Info.plist` 파일을 다운로드하고 프로젝트에 추가합니다.
4. Firebase SDK를 설정합니다. `AppDelegate.swift` 파일에 다음과 같은 코드를 추가합니다.

```swift
import Firebase

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

## 2. 푸시 알림 권한 요청

iOS에서 푸시 알림을 보내기 위해서는 사용자에게 알림 권한을 요청해야 합니다. 이를 위해 `UNUserNotificationCenter`를 사용합니다. `AppDelegate.swift` 파일에 다음의 코드를 추가합니다.

```swift
import UserNotifications

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()

    UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
        if granted {
            DispatchQueue.main.async {
                application.registerForRemoteNotifications()
            }
        }
    }

    return true
}
```

## 3. 디바이스 토큰 가져오기

푸시 알림을 받으려면 앱을 설치한 디바이스의 토큰을 가져와야 합니다. 이 토큰은 FCM을 통해 푸시 알림을 보내는 데 사용됩니다. `AppDelegate.swift` 파일에 다음의 코드를 추가합니다.

```swift
func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    print("Device Token:", token)
}
```

## 4. 푸시 알림 수신 처리

FCM을 통해 보낸 푸시 알림을 앱에서 처리하려면 `UNUserNotificationCenterDelegate`를 구현해야 합니다. `AppDelegate.swift` 파일에 다음의 코드를 추가합니다.

```swift
extension AppDelegate: UNUserNotificationCenterDelegate {
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.alert, .badge, .sound])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
        // 푸시 알림을 눌렀을 때 실행될 코드를 작성합니다.
        completionHandler()
    }
}
```

## 5. 푸시 알림 테스트

위의 단계를 모두 완료한 후 앱을 빌드하고 디바이스에 설치합니다. Firebase 콘솔에서 푸시 알림을 보내기 위한 테스트를 할 수 있습니다. 또는 서버에서 FCM을 통해 푸시 알림을 보낼 수도 있습니다.

이제 Firebase Cloud Messaging을 사용하여 iOS 앱에 푸시 알림을 구현할 수 있습니다. FCM은 강력하고 유연한 푸시 알림 서비스이며, 개발자가 사용자에게 중요한 정보를 빠르게 전달할 수 있게 해줍니다. 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/cloud-messaging)를 참조하세요.

Happy coding!