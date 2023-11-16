---
layout: post
title: "[swift] Swift에서 Firebase Crashlytics를 사용한 앱 크래시 리포팅"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Crashlytics는 앱의 크래시 로그를 실시간으로 수집하고 분석하여 앱 개발자에게 크래시의 원인을 신속하게 파악할 수 있는 도구입니다. 이번 글에서는 Swift에서 Firebase Crashlytics를 사용하여 앱 크래시 리포팅을 설정하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. [Firebase 콘솔](https://console.firebase.google.com/)에 로그인하고 프로젝트를 생성합니다.
2. Firebase 프로젝트에 iOS 앱을 추가합니다.
3. `GoogleService-Info.plist` 파일을 다운로드하고 프로젝트에 추가합니다.

## Firebase SDK 설치

1. Firebase SDK를 사용하기 위해 `Podfile`에 다음과 같은 팟을 추가합니다.

```swift
platform :ios, '11.0'
use_frameworks!

target 'YourAppName' do
  pod 'Firebase/Crashlytics'
end
```

2. 터미널에서 `pod install` 명령어를 실행하여 Firebase SDK를 설치합니다.

## Crashlytics 초기화

1. 앱의 `AppDelegate.swift` 파일에서 `import Firebase`을 추가합니다.
2. `didFinishLaunchingWithOptions` 메서드 내부에 다음 코드를 추가하여 Crashlytics를 초기화합니다.

```swift
FirebaseApp.configure()
Fabric.sharedSDK().debug = true  // 개발 중에는 디버그 모드를 사용합니다.
Crashlytics.sharedInstance().delegate = self
```

3. AppDelegate 클래스에서 `CrashlyticsDelegate` 프로토콜을 구현합니다.

```swift
extension AppDelegate: CrashlyticsDelegate {
    func crashlyticsDidDetectReport(forLastExecution report: CLSReport, completionHandler: @escaping (Bool) -> Void) {
        // 앱이 크래시되었을 때 실행되는 동작을 구현합니다.
        // 예를 들어, 사용자에게 앱이 크래시되었다는 알림을 보낼 수 있습니다.
        // completionHandler를 호출하여 Crashlytics에 리포트 전송 여부를 알려줍니다.
        completionHandler(true)
    }
}
```

4. 앱이 크래시되었을 때 Crashlytics에 리포트를 전송하도록 설정합니다. 
`didFinishLaunchingWithOptions` 메서드에서 다음 코드를 추가해주세요.

```swift
Crashlytics.sharedInstance().setCrashlyticsCollectionEnabled(true)
Fabric.with([Crashlytics.self])
```


## Crashlytics를 사용한 리포트

1. Crashlytics에 커스텀 이벤트를 기록합니다.

```swift
Crashlytics.sharedInstance().log("Custom Event")
```

2. 크래시 리포트에 사용자 정보를 추가합니다.

```swift
Crashlytics.sharedInstance().setUserIdentifier("user123")
Crashlytics.sharedInstance().setUserName("John Doe")
Crashlytics.sharedInstance().setUserEmail("johndoe@example.com")
```

3. 사용자가 대화식 디버그 정보를 제공할 수 있도록 합니다.

```swift
Crashlytics.sharedInstance().setObjectValue("Value", forKey: "Key")
Crashlytics.sharedInstance().setIntValue(10, forKey: "IntValue")
Crashlytics.sharedInstance().setBoolValue(true, forKey: "BoolValue")
Crashlytics.sharedInstance().setFloatValue(3.14, forKey: "FloatValue")
Crashlytics.sharedInstance().setUserValue("Value", forKey: "Key")
Crashlytics.sharedInstance().recordCustomExceptionName("CustomException", reason: "Reason", frameArray: [])
```

4. 특정 상황에서 예외 처리를 위해 다음과 같이 예외를 기록할 수 있습니다.

```swift
Crashlytics.sharedInstance().recordError(error)
```

5. 원격 구성을 사용하여 앱을 제어하려면 다음을 수행합니다.

```swift
Crashlytics.sharedInstance().setCrashlyticsCollectionEnabled(false)
Crashlytics.sharedInstance().setCustomValue("Value", forKey: "Key")
```

이제 Firebase Crashlytics를 사용하여 앱의 크래시 리포트를 실시간으로 수집하고 분석할 수 있습니다. 앱을 개발하는 동안 발생하는 크래시를 신속하게 파악하고 수정하여 사용자 경험을 향상시킬 수 있습니다.

참조:
- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [Firebase 콘솔](https://console.firebase.google.com/)
- [Fabric 문서](https://docs.fabric.io/)