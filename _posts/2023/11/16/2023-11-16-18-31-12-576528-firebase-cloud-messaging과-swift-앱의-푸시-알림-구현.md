---
layout: post
title: "[swift] Firebase Cloud Messaging과 Swift 앱의 푸시 알림 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging은 앱으로 푸시 알림을 보낼 수 있는 강력한 도구입니다. 이 기능을 Swift 앱에서 구현하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase 콘솔에 로그인한 후, 새로운 프로젝트를 생성합니다. 프로젝트 설정에서 iOS 앱을 추가하고, Bundle ID를 입력합니다. 이때, 앱 등록 시에 케이스 센서티브 문자열이어야 합니다.

Firebase iOS 설정 파일인 `GoogleService-Info.plist`를 다운로드합니다. 이 파일은 나중에 Swift 앱에서 Firebase에 연결하기 위해 사용됩니다.

## 2. Swift 앱에 Firebase 설정

Xcode에서 Swift 앱 프로젝트를 엽니다. Firebase를 사용하려면, Firebase SDK를 프로젝트에 추가해야 합니다.

Firebase SDK를 설치하기 위해 `Podfile`에 다음 줄을 추가합니다.

```swift
pod 'Firebase/Core'
pod 'Firebase/Messaging'
```

터미널을 열고 프로젝트 루트 폴더에서 `pod install` 명령어를 실행합니다. 이 명령어를 통해 Firebase SDK의 최신 버전이 프로젝트에 설치됩니다.

## 3. AppDelegate 수정

AppDelegate.swift 파일을 열고 다음 코드를 추가합니다.

```swift
import Firebase

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        FirebaseApp.configure()
        
        // iOS 10 이상에서 사용되는 코드
        if #available(iOS 10.0, *) {
            let authOptions: UNAuthorizationOptions = [.alert, .badge, .sound]
            UNUserNotificationCenter.current().requestAuthorization(options: authOptions, completionHandler: { _, _ in })
            
            // 앱이 백그라운드에서 실행되는 동안 푸시 알림을 처리하는 코드
            Messaging.messaging().delegate = self
            UNUserNotificationCenter.current().delegate = self
        } else {
            let settings: UIUserNotificationSettings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)
            application.registerUserNotificationSettings(settings)
        }
        
        application.registerForRemoteNotifications()
        
        return true
    }
    
    // 푸시 알림 등록이 성공한 경우 호출되는 메소드
    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        Messaging.messaging().apnsToken = deviceToken
    }
    
    // 푸시 알림을 수신한 경우 호출되는 메소드
    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
        Messaging.messaging().appDidReceiveMessage(userInfo)
        completionHandler(UIBackgroundFetchResult.newData)
    }
}

// iOS 10 이상에서 사용되는 코드
@available(iOS 10, *)
extension AppDelegate: UNUserNotificationCenterDelegate, MessagingDelegate {
    
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.banner, .badge, .sound])
    }
    
    func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {
        // 푸시 알림 등록 토큰을 가져온 후에 추가적인 작업을 수행할 수 있습니다.
    }
}
```

위의 코드는 앱이 시작될 때 Firebase를 구성하고, 푸시 알림 등록과 메시지 수신을 처리하는 방법을 보여줍니다.

## 4. 푸시 알림 보내기

Firebase 콘솔에서 푸시 알림을 보내려는 앱의 프로젝트로 이동합니다. "Cloud Messaging" 탭에서 "새 알림 작성" 버튼을 클릭합니다.

알림을 보낼 대상을 선택한 후, 푸시 알림 내용을 작성합니다. 이때, Advanced Options에서 "알림을 특정 앱으로 보냄"을 선택하고, 앱의 Bundle ID를 입력해야 합니다.

## 마무리

이제 Firebase Cloud Messaging과 Swift 앱에서 푸시 알림을 보내고 받을 수 있습니다. Firebase의 강력한 기능을 활용하여 사용자에게 중요한 알림을 전달할 수 있습니다.

더 자세한 내용은 [Firebase 문서](https://firebase.google.com/docs/cloud-messaging)를 참조하시기 바랍니다.