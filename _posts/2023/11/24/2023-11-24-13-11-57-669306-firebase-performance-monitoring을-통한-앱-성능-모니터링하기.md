---
layout: post
title: "[swift] Firebase Performance Monitoring을 통한 앱 성능 모니터링하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Performance Monitoring은 앱의 성능을 실시간으로 모니터링하여 사용자 경험을 개선할 수 있는 강력한 도구입니다. 이를 통해 앱의 네트워크 요청, 데이터베이스 쿼리, 화면 전환 등의 작업을 추적하고 성능에 영향을 주는 병목 현상을 식별할 수 있습니다. 이번에는 Firebase Performance Monitoring을 Swift 앱에 통합하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정하기

Firebase Performance Monitoring을 사용하기 위해 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에 접속한 후 "프로젝트 추가"를 선택하여 프로젝트를 생성해 주세요. 프로젝트 생성이 완료되면 Firebase SDK 설정 단계로 진행합니다.

## 2. Firebase SDK 설정하기

Firebase을 사용하기 위해 iOS 앱에 Firebase SDK를 추가해야 합니다. 하지만 Firebase Performance Monitoring은 별도의 SDK 추가가 필요하지 않습니다. Firebase SDK를 이미 추가한 경우, Firebase Performance Monitoring은 자동으로 포함됩니다. 

## 3. Firebase Performance Monitoring 초기화하기

Firebase Performance Monitoring을 사용하려면 앱이 구동될 때 초기화를 해야 합니다. AppDelegate.swift 파일의 `application(_:didFinishLaunchingWithOptions:)` 메서드에 다음 코드를 추가해 주세요.

```swift
import Firebase
import FirebasePerformance

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    FirebasePerformance.sharedInstance().instrumentationEnabled = true
    
    return true
}
```

위 코드는 Firebase SDK를 초기화한 다음, Firebase Performance Monitoring을 활성화하는 역할을 수행합니다.

## 4. 사용자 정의 트레이스 생성하기

Firebase Performance Monitoring은 자동으로 앱의 네트워크 요청, 데이터베이스 쿼리 등의 지표를 추적합니다. 하지만 특정 작업의 성능을 개별적으로 추적하려면 사용자 정의 트레이스를 생성해야 합니다.

아래는 사용자 정의 트레이스를 생성하는 예시 코드입니다.

```swift
import FirebasePerformance

let trace = Performance.startTrace(name: "MyCustomTrace")
// 해당 작업 수행

trace.stop()
```

위 코드에서는 `startTrace(name:)` 메서드를 사용하여 사용자 정의 트레이스를 시작하고, 작업을 수행한 후 `stop()` 메서드로 트레이스를 종료합니다.

## 5. 성능 지표 확인하기

Firebase 콘솔에서는 Firebase Performance Monitoring을 통해 수집된 성능 지표를 확인할 수 있습니다. 앱의 네트워크 요청, 데이터베이스 쿼리, 화면 전환 등의 작업에 대한 성능 데이터를 실시간으로 모니터링하고 병목 현상을 식별하여 앱의 성능을 개선할 수 있습니다.

## 결론

Firebase Performance Monitoring은 앱의 성능을 실시간으로 모니터링하고 성능에 영향을 주는 병목 현상을 식별할 수 있는 강력한 도구입니다. Firebase Performance Monitoring을 Swift 앱에 통합하여 앱의 성능을 개선해 보세요.

## 참고 자료

- [Firebase Performance Monitoring 문서](https://firebase.google.com/docs/perf-mon?hl=ko)
- [Swift와 Firebase 통합하기](https://firebase.google.com/docs/ios/setup?hl=ko)