---
layout: post
title: "[swift] Swift에서 Firebase의 Firebase Cloud Messaging을 이용한 푸시 알림 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging(FCM)은 개발자가 안드로이드 및 iOS 앱으로 푸시 알림을 보낼 수 있도록 하는 Firebase의 기능입니다. 이 기능을 Swift 앱에서 사용하여 푸시 알림을 구현하는 방법을 알아보겠습니다.

## Firebase 설정

1. [Firebase 콘솔](https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성합니다.
2. iOS 앱을 추가하고, Bundle Identifier를 입력합니다.
3. GoogleService-Info.plist 파일을 다운로드하여 프로젝트에 추가합니다.
4. CocoaPods를 사용하여 Firebase Messaging을 설치합니다.

```swift
pod 'Firebase/Messaging'
```

5. 터미널에서 `pod install` 명령어를 실행하여 프로젝트에 Firebase Messaging을 추가합니다.

## AppDelegate 설정

AppDelegate.swift 파일을 열고 다음 코드를 추가합니다.

```swift
import UIKit
import Firebase

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        FirebaseApp.configure()
        Messaging.messaging().delegate = self
        
        // 푸시 알림 등록
        registerForPushNotifications()
        
        return true
    }
    
    // APNs 등록 코드
    func registerForPushNotifications() {
        if #available(iOS 10.0, *) {
            UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .badge, .sound]) { (granted, error) in
                guard granted else { return }
                DispatchQueue.main.async {
                    UIApplication.shared.registerForRemoteNotifications()
                }
            }
        } else {
            let userNotificationTypes: UIUserNotificationType = [.alert, .badge, .sound]
            let settings = UIUserNotificationSettings(types: userNotificationTypes, categories: nil)
            UIApplication.shared.registerUserNotificationSettings(settings)
            UIApplication.shared.registerForRemoteNotifications()
        }
    }
    
    // 푸시 알림 등록 후 토큰 받아오기
    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
        print("푸시 알림 등록 성공. 토큰: \(token)")
        
        // Firebase에 토큰 등록
        Messaging.messaging().apnsToken = deviceToken
    }
    
    // 푸시 알림 수신 처리
    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any]) {
        print("푸시 알람 수신: \(userInfo)")
    }
}

// MessagingDelegate 구현
extension AppDelegate: MessagingDelegate {
    func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
        print("Firebase 토큰 갱신: \(fcmToken)")
        
        // 앱 서버로 토큰 전송
        sendRegistrationToServer(fcmToken)
    }
    
    func messaging(_ messaging: Messaging, didReceive remoteMessage: MessagingRemoteMessage) {
        print("푸시 메시지 받음: \(remoteMessage.appData)")
    }
    
    func sendRegistrationToServer(_ fcmToken: String) {
        // 앱 서버로 토큰 전송하는 로직 구현
    }
}
```

위의 코드는 AppDelegate 클래스에 Firebase 설정 및 푸시 알림 처리 기능을 추가하는 코드입니다.

## 푸시 알림 보내기

Firebase 콘솔로 돌아가서 Cloud Messaging 탭을 엽니다. '새 알림 보내기' 버튼을 클릭하고 알림 제목 및 내용을 입력합니다. 이후 대상을 선택하여 알림을 보낼 수 있습니다.

## 결론

위의 단계를 따라 Swift 앱에서 Firebase Cloud Messaging을 사용하여 푸시 알림을 구현할 수 있습니다. Firebase는 매우 강력한 푸시 알림 서비스이며, 사용하기 쉬운 API와 콘솔을 제공합니다.

Firebase 공식 [문서](https://firebase.google.com/docs/cloud-messaging)를 참조하여 더 자세한 내용을 확인하십시오.