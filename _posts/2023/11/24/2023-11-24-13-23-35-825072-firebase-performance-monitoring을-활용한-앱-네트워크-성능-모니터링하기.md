---
layout: post
title: "[swift] Firebase Performance Monitoring을 활용한 앱 네트워크 성능 모니터링하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Firebase Performance Monitoring을 활용하여 iOS 앱의 네트워크 성능을 모니터링하는 방법에 대해 알아보겠습니다. Firebase Performance Monitoring은 앱의 성능을 지속적으로 모니터링하고 개선할 수 있는 도구입니다.

Firebase Performance Monitoring을 사용하기 위해서는 Firebase를 프로젝트에 추가하고 Firebase Performance Monitoring SDK를 설치해야 합니다. Firebase를 프로젝트에 추가하는 방법은 Firebase 공식 문서를 참고하시면 됩니다.

## Firebase Performance Monitoring SDK 설치

Firebase Performance Monitoring SDK를 설치하기 위해 `Podfile` 파일에 다음과 같이 Firebase Performance Monitoring 라이브러리를 추가하세요.

```swift
pod 'Firebase/Performance'
```

설치가 완료되었다면, `Podfile`이 있는 디렉토리에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드 및 설치하세요.

## 네트워크 성능 모니터링 설정

1. AppDelegate에서 Firebase를 초기화하세요.

```swift
import Firebase

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    // ...
    return true
}
```

2. 네트워크 호출을 시작하기 전과 종료한 후에 `FIRTrace` 객체를 사용하여 성능 정보를 검색하세요. 

```swift
import FirebasePerformance

// 네트워크 호출 시작
let trace = Performance.startTrace(name: "NetworkRequest")

// 네트워크 요청 코드

// 네트워크 호출 종료
trace?.stop()
```

3. 네트워크 요청 중에 추가 정보를 기록하려면 `FIRTrace` 객체의 `incrementMetric:byInt:` 메서드를 사용하세요.

```swift
// 추가 정보 기록 예시
trace?.incrementMetric("ImageSize", by: image.size)
```

## 성능 데이터 확인하기

Firebase 콘솔에서 Firebase Performance Monitoring 섹션으로 이동하여 앱의 성능 데이터를 확인할 수 있습니다. 여기서는 네트워크 요청의 지연 시간, 성공률, 추가 정보 등을 확인할 수 있어 앱의 성능을 실시간으로 모니터링하고 개선할 수 있습니다.

## 결론

Firebase Performance Monitoring을 사용하면 앱의 네트워크 성능을 측정하고 모니터링할 수 있습니다. 이를 통해 개발자는 앱의 성능을 실시간으로 이해하고 최적화할 수 있으며, 사용자들이 향상된 앱 사용 경험을 누릴 수 있습니다.

더 많은 정보와 세부 설정은 [Firebase 공식 문서](https://firebase.google.com/docs/perf-mon)를 참고하시기 바랍니다.