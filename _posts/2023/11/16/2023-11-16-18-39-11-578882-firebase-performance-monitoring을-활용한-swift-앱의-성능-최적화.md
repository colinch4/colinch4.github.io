---
layout: post
title: "[swift] Firebase Performance Monitoring을 활용한 Swift 앱의 성능 최적화"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Performance Monitoring은 앱의 성능을 측정하고 최적화할 수 있는 강력한 도구입니다. 이 도구를 활용하여 Swift 앱의 성능을 향상시킬 수 있습니다. 이번 블로그 포스트에서는 Firebase Performance Monitoring을 Swift 앱에 통합하는 방법과 몇 가지 성능 최적화 기법을 알아보겠습니다.

## Firebase Performance Monitoring 통합하기

1. Firebase Console에서 프로젝트를 만들고 앱을 추가합니다.
2. Firebase iOS SDK를 프로젝트에 추가합니다. Cocoapods를 사용한다면 `pod 'Firebase/Performance'`를 `Podfile`에 추가하고 `pod install` 명령을 실행합니다.
3. `AppDelegate.swift` 파일을 열고 `import Firebase` 코드를 추가합니다.
4. `didFinishLaunchingWithOptions` 메서드에서 `FirebaseApp.configure()`를 호출합니다.

```swift
import Firebase

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        FirebaseApp.configure()
        // other setup code
        return true
    }

    // ...
}
```

Firebase Performance Monitoring의 기본 설정은 이미 완료되었습니다. 이제 성능을 측정할 영역을 식별하고 모니터링을 시작할 준비를 해야합니다.

## 성능 측정 및 최적화 기법

### Transaction 모니터링

Firebase Performance Monitoring은 앱의 특정 영역을 트랜잭션이라는 단위로 구분하여 성능을 측정합니다. 트랜잭션은 앱 내에서 진행되는 작업의 범주를 의미합니다. 예를 들어, 화면 전환, 데이터베이스 쿼리, 네트워크 요청 등의 작업을 각각 다른 트랜잭션으로 정의할 수 있습니다.

```swift
import FirebasePerformance

// 트랜잭션 시작
let transaction = Performance.startTrace(name: "Login")

// 트랜잭션 시간 측정
// ...

// 트랜잭션 완료
transaction?.stop()
```

위 코드에서는 "Login"이라는 이름으로 트랜잭션을 시작하고, 트랜잭션의 실행 시간을 측정한 뒤 트랜잭션을 완료합니다. 이렇게 측정한 트랜잭션들은 Firebase Console에서 확인할 수 있습니다.

### 네트워크 요청 최적화

네트워크 요청은 앱의 성능에 큰 영향을 미칠 수 있습니다. Firebase Performance Monitoring을 사용하여 실제 네트워크 요청의 성능을 측정하고 최적화할 수 있습니다.

```swift
import FirebasePerformance

let url = URL(string: "https://example.com/api/data")
let request = URLRequest(url: url!)

// 네트워크 요청 트랜잭션 시작
let transaction = Performance.startTrace(name: "Network Request")

URLSession.shared.dataTask(with: request) { (data, response, error) in
    // 네트워크 요청 시간 측정 및 처리
    // ...
    
    // 네트워크 요청 트랜잭션 완료
    transaction?.stop()
}.resume()
```

위 코드에서는 네트워크 요청을 보내기 전에 트랜잭션을 시작하고, 데이터를 받은 후에 트랜잭션을 완료합니다. 이렇게 측정된 네트워크 요청의 성능은 Firebase Console에서 확인할 수 있습니다.

### 앱 크래시 추적

Firebase Performance Monitoring은 앱이 크래시되었을 때 크래시를 추적하고 원인을 분석할 수 있는 기능도 제공합니다. 이를 활용하여 앱의 안정성을 향상시킬 수 있습니다.

```swift
import FirebaseCrashlytics

Crashlytics.crashlytics().setCrashlyticsCollectionEnabled(true)

// ...

func applicationDidReceiveMemoryWarning(_ application: UIApplication) {
    Crashlytics.crashlytics().log("Received memory warning")
    Crashlytics.crashlytics().record(error: NSError(domain: "", code: 0, userInfo: nil))
}
```

위 코드에서는 `applicationDidReceiveMemoryWarning` 메서드를 사용하여 메모리 경고를 받았을 때 크래시 로그를 기록합니다. Firebase Console에서 이 로그를 확인하고 크래시의 원인을 분석할 수 있습니다.

## 마무리

이제 Firebase Performance Monitoring을 활용하여 Swift 앱의 성능을 측정하고 최적화할 수 있는 방법을 알아보았습니다. Firebase Performance Monitoring을 적절하게 활용하면 앱의 성능을 개선하고 사용자 경험을 향상시킬 수 있습니다.