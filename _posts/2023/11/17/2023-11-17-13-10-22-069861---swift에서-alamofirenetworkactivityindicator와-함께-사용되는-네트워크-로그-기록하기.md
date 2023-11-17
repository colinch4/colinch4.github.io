---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator와 함께 사용되는 네트워크 로그 기록하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 개발 중 네트워크 통신 시 로그를 기록하는 것은 매우 중요합니다. 이를 통해 통신 동작을 추적하고 문제 발생 시 원인을 파악할 수 있습니다. 이번 글에서는 AlamofireNetworkActivityIndicator와 함께 Swift에서 네트워크 로그를 기록하는 방법에 대해 알아보겠습니다.

## AlamofireNetworkActivityIndicator란?

AlamofireNetworkActivityIndicator는 Alamofire의 확장 라이브러리로, 네트워크 요청이 진행 중일 때 상태 바의 인디케이터를 표시하는 기능을 제공합니다. 이 기능은 사용자에게 네트워크 통신이 진행되고 있는지 시각적으로 알려주어 사용자 경험을 향상시킬 수 있습니다.

## 네트워크 로그 기록하기

네트워크 로그를 기록하기 위해 먼저 `AlamofireNetworkActivityIndicator`을 설치해야 합니다. `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'AlamofireNetworkActivityIndicator'
```

설치 후, 프로젝트를 빌드하고 `AppDelegate.swift` 파일을 엽니다. 다음과 같이 `import AlamofireNetworkActivityIndicator`를 추가해줍니다.

```swift
import AlamofireNetworkActivityIndicator
```

이제 `application(_:didFinishLaunchingWithOptions:)` 메서드에서 `networkActivityIndicatorManager.isEnabled`를 true로 설정해 네트워크 인디케이터를 활성화합니다.

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // ...
    NetworkActivityIndicatorManager.shared.isEnabled = true
    // ...
    return true
}
```

이제 네트워크 로그를 기록하기 위한 `SessionDelegate` 클래스를 만듭니다. 이 클래스를 사용하면 Alamofire가 수행하는 통신 동작을 추적하여 로그로 기록할 수 있습니다.

```swift
class LogSessionDelegate: SessionDelegate {
    override func taskDidResume(_ task: URLSessionTask) {
        super.taskDidResume(task)
        print("Task Resumed: \(task)")
    }
    
    override func taskDidComplete(_ task: URLSessionTask, error: Error?) {
        super.taskDidComplete(task, error: error)
        if let error = error {
            print("Task Completed with Error: \(error.localizedDescription)")
        } else {
            print("Task Completed Successfully")
        }
    }
}
```

이제 `AppDelegate.swift` 파일에서 `logSessionDelegate` 변수를 추가하고, `URLSessionConfiguration`에 `delegate` 속성으로 설정합니다.

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    // ...
    
    var logSessionDelegate = LogSessionDelegate()
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        NetworkActivityIndicatorManager.shared.isEnabled = true
        let configuration = URLSessionConfiguration.default
        configuration.timeoutIntervalForRequest = 30
        configuration.timeoutIntervalForResource = 30
        configuration.urlCache = nil
        configuration.httpAdditionalHeaders = Alamofire.SessionManager.defaultHTTPHeaders
        configuration.httpAdditionalHeaders?["Content-Type"] = "application/json"
        configuration.protocolClasses?.insert(HTTPLogger.self, at: 0)
        configuration.protocolClasses?.insert(HTTPDelayProtocol.self, at: 0)
        configuration.protocolClasses?.insert(HTTPCacheableProtocol.self, at: 0)
        configuration.protocolClasses?.insert(HTTPNoCacheProtocol.self, at: 0)
        configuration.protocolClasses?.insert(NetworkPinningProtocol.self, at: 0)
        configuration.protocolClasses?.insert(SocksProxyProtocol.self, at: 0)
        configuration.protocolClasses?.insert(logSessionDelegate, at: 0) // Add LogSessionDelegate
        // ...
        return true
    }

    // ...
}
```

코드를 실행하고 네트워크 요청을 하면, 콘솔에 각 통신 동작에 대한 로그가 출력됩니다.

## 마무리

이번 글에서는 AlamofireNetworkActivityIndicator와 함께 Swift에서 네트워크 로그를 기록하는 방법에 대해 알아보았습니다. 네트워크 로그를 통해 문제 발생 시 원인을 파악하고 디버깅에 도움을 받을 수 있습니다. 앱 개발시 네트워크 로그를 기록하는 습관을 가지고 진행하면 더 효과적인 디버깅이 가능해질 것입니다.

## 참고 자료

- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/josejuanqm/AlamofireNetworkActivityIndicator)