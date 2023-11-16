---
layout: post
title: "[swift] Firebase의 Performance Monitoring과 Swift 프로파일링 도구의 연동 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Performance Monitoring은 앱의 성능을 측정하고 분석하는 도구입니다. Swift 프로파일링 도구와 함께 사용하면 앱의 성능 개선에 도움이 될 수 있습니다. 이번 글에서는 Firebase의 Performance Monitoring을 Swift 프로파일링 도구와 연동하는 방법을 알아보겠습니다.

## Performance Monitoring 설정

1. Firebase 콘솔에서 앱을 선택하고 Performance 텝으로 이동합니다.
2. "Performance Monitoring 설정"으로 이동하여 iOS 앱으로 설정합니다.
3. Firebase SDK를 추가합니다. `pod 'Firebase/Performance'`을 `Podfile`에 추가하고 터미널에서 `pod install`을 실행합니다.
4. `AppDelegate.swift` 파일에서 Firebase를 초기화합니다. 

```swift
import Firebase

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

## Swift 프로파일링 도구 설정

Firebase Performance Monitoring은 앱 실행 중에 성능 데이터를 수집합니다. Swift 프로파일링 도구는 이 데이터를 수집하여 시각화하고 분석하는 데 사용됩니다. Swift 프로파일링 도구를 사용하려면 다음 단계를 따르세요.

1. Xcode를 열고 `Product > Scheme > Edit Scheme...`에서 `Profile`을 선택합니다.
2. `Instrument` 기능을 사용하여 프로파일링 도구를 실행합니다.
3. `Profile` 메뉴에서 `Performance`을 선택한 후, 앱을 실행합니다.

여기까지 따라오셨다면 Firebase Performance Monitoring과 Swift 프로파일링 도구를 연동한 준비가 완료되었습니다.

## Performance Monitoring 사용하기

지금은 앱을 프로파일링하는 동안 Performance Monitoring이 활성화되어 있지 않습니다. 따라서 성능 데이터를 수집하려면 다음과 같이 몇 가지 변경을 해야 합니다.

1. `AppDelegate.swift` 파일에서 `FirebasePerformance`을 import 합니다.

```swift
import FirebasePerformance
```

2. `application(_:didFinishLaunchingWithOptions:)` 메서드에서 `FirebasePerformance`을 초기화합니다.

```swift
import FirebasePerformance

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    FirebasePerformance.initialize()
    return true
}
```

3. 원하는 곳에 Custom Trace를 추가하여 성능 데이터를 수집할 수 있습니다.

```swift
import FirebasePerformance

func myCustomFunction() {
    let trace = Performance.startTrace(name: "myCustomFunction")
    // Custom logic here
    trace.stop()
}
```

위의 예제에서 `myCustomFunction`은 성능 데이터 추적을 시작하고 멈추는 데 사용됩니다. 이 자리에 원하는 로직을 추가하여 성능 데이터를 수집할 수 있습니다.

## 결론

Firebase Performance Monitoring과 Swift 프로파일링 도구를 연동하여 앱의 성능을 측정하고 분석하는 것은 앱 개발 과정에서 중요한 역할을 합니다. Firebase와 Swift의 조합은 앱의 성능 개선에 매우 유용한 도구들을 제공합니다. 이번 글을 통해 Firebase Performance Monitoring과 Swift 프로파일링 도구의 연동 방법에 대해 알아보았습니다.

참고 문서:
- [Firebase Performance Monitoring 문서](https://firebase.google.com/docs/perf-mon)
- [Swift Instruments 문서](https://developer.apple.com/documentation/xcode/using_instruments_to_improve_your_code)