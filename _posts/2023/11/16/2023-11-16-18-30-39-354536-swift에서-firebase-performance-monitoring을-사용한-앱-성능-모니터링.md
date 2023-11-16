---
layout: post
title: "[swift] Swift에서 Firebase Performance Monitoring을 사용한 앱 성능 모니터링"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 성능은 사용자 경험에 매우 중요합니다. Firebase Performance Monitoring을 사용하면 앱의 성능을 측정하고 모니터링할 수 있습니다. 이 블로그 포스트에서는 Firebase Performance Monitoring을 사용하여 Swift 앱의 성능을 모니터링하는 방법을 안내하겠습니다.

## Firebase Performance Monitoring 설정하기

1. Firebase 콘솔에 로그인하고 프로젝트를 선택합니다.
2. "프로젝트 설정"으로 이동한 다음 "서비스 계정" 탭을 선택합니다.
3. "새 비공개 키 생성" 버튼을 클릭하여 서비스 계정 JSON 파일을 다운로드합니다.

## Swift 프로젝트에 Firebase Performance Monitoring 추가하기

1. Firebase 콘솔에서 다운로드한 서비스 계정 JSON 파일을 프로젝트의 루트 폴더에 추가합니다.
2. 프로젝트의 Podfile을 열고 다음 줄을 추가합니다:
   ```
   pod 'Firebase/Performance'
   ```
3. 터미널에서 `pod install` 명령어를 실행하여 Firebase Performance Monitoring을 포함한 Firebase SDK를 설치합니다.

## Firebase Performance Monitoring 초기화하기

앱에서 Firebase Performance Monitoring을 사용하려면 초기화해야 합니다. 앱이 시작될 때 FirebaseApp을 초기화하고 FirebasePerformance 인스턴스를 만들어야 합니다. iOS 앱에서는 일반적으로 AppDelegate.swift 파일에서 초기화 작업을 수행합니다.

```swift
import Firebase

class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        FirebaseApp.configure()
        let performance = FirebasePerformance.sharedInstance()
        performance?.start()
        return true
    }
}
```

위의 예제에서는 `FirebaseApp.configure()`를 사용하여 FirebaseApp을 초기화하고 `FirebasePerformance.sharedInstance().start()`를 사용하여 Firebase Performance Monitoring을 시작합니다.

## Custom Trace 추가하기

앱의 성능을 추적하려면 Custom Trace를 추가해야 합니다. Custom Trace는 앱의 특정 부분에 대한 성능 데이터를 제공합니다. 예를 들어, 특정 함수의 실행 시간을 측정하고 싶다면 해당 함수 시작과 끝에 Custom Trace를 추가해야 합니다.

```swift
import FirebasePerformance

func myFunction() {
    let trace = Performance.startTrace(name: "myFunction")
    
    // myFunction 코드
    
    trace.stop()
}
```

위의 예제에서는 `Performance.startTrace()`를 사용하여 새로운 Custom Trace를 시작하고 `trace.stop()`를 사용하여 Custom Trace를 종료합니다. `name` 매개변수에는 Custom Trace의 이름을 지정합니다.

## 뷰 로딩 시간 측정하기

Firebase Performance Monitoring을 사용하여 뷰의 로딩 시간을 측정할 수도 있습니다. UIViewController의 viewDidLoad() 메서드에서 Custom Trace를 시작하고 viewDidAppear(_:) 메서드에서 Custom Trace를 종료하여 뷰의 로딩 시간을 측정합니다.

```swift
import FirebasePerformance

class MyViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let trace = Performance.startTrace(name: "MyViewController")
        
        // viewDidLoad() 코드
        
        trace.incrementMetric("viewDidLoad", by: ProcessInfo.processInfo.systemUptime)
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        trace.stop()
    }

}
```

위의 예제에서는 `viewDidLoad()`에서 Custom Trace를 시작하고 `viewDidAppear()`에서 Custom Trace를 종료합니다. 또한 `trace.incrementMetric(_:by:)`를 사용하여 viewDidAppear() 호출까지 걸린 시간을 측정하고 Custom Metric으로 기록합니다.

## Firebase Performance Monitoring 데이터 확인하기

Firebase 콘솔에서 Firebase Performance Monitoring을 사용하여 앱의 성능 데이터를 확인할 수 있습니다. Firebase 콘솔에서 앱을 선택한 후 "Performance" 탭을 선택하면 성능 데이터를 확인할 수 있습니다. 여기서는 앱의 Custom Traces 및 Custom Metrics에 대한 데이터 및 그래프를 확인할 수 있습니다.

## 마무리

이제 Swift 앱에서 Firebase Performance Monitoring을 사용하여 앱의 성능을 모니터링할 수 있는 방법을 알게 되었습니다. Firebase Performance Monitoring은 앱의 성능을 측정하고 최적화하는 데 도움을 줄 수 있는 강력한 도구입니다. 자세한 내용은 [Firebase Performance Monitoring 문서](https://firebase.google.com/docs/perf-mon)를 참조하세요.