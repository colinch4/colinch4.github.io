---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 사용하여 네트워크 에러 발생 시 로그 파일에 기록하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

많은 앱은 네트워크 요청 중에 사용자에게 활동 중임을 나타내기 위해 네트워크 인디케이터를 표시합니다. Alamofire는 네트워크 요청 중에 네트워크 인디케이터를 자동으로 관리하는 `AlamofireNetworkActivityIndicator`을 제공합니다. 그러나 기본적으로 Alamofire는 네트워크 에러가 발생해도 네트워크 인디케이터를 숨기지 않습니다.

이 문제를 해결하기 위해, 네트워크 에러가 발생할 때마다 에러 정보를 로그 파일에 기록할 수 있는 로깅 시스템을 구현해볼 것입니다.

## AlamofireNetworkActivityIndicator 설정

먼저, AlamofireNetworkActivityIndicator를 설정하기 위해 다음 코드 스니펫을 AppDelegate.swift 파일의 `application(_:didFinishLaunchingWithOptions:)` 메서드에 추가합니다.

```swift
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    NetworkActivityIndicatorManager.shared.isEnabled = true
    NetworkActivityIndicatorManager.shared.startDelay = 0.1

    return true
}
```

위 코드는 앱이 시작될 때 AlamofireNetworkActivityIndicator를 활성화하고, 네트워크 요청이 시작되기 전에 인디케이터를 표시하기 위한 지연을 설정합니다.

## 네트워크 에러 로깅

이제 네트워크 에러가 발생할 때마다 에러 정보를 로그 파일에 기록하는 기능을 추가해보겠습니다. Alamofire는 네트워크 응답 결과를 처리하기 위해 `response` 메서드를 제공합니다. 이 메서드를 사용하여 네트워크 요청의 성공 또는 실패 여부를 확인할 수 있습니다.

먼저, 사용자 정의 로깅 클래스를 만들고, 네트워크 에러가 발생할 때 호출될 `logError` 메서드를 추가합니다.

```swift
class Logger {
    static func logError(request: URLRequest?, error: Error) {
        // 에러 정보를 로그 파일에 기록하는 코드를 추가하세요.
    }
}
```

그런 다음, Alamofire의 `response` 메서드로 네트워크 요청을 보냅니다.

```swift
AF.request(urlString).response { response in
    switch response.result {
    case .success(let data):
        // 성공적인 응답 처리
    case .failure(let error):
        Logger.logError(request: response.request, error: error)
    }
}
```

위 코드에서, 응답이 성공한 경우에는 `data`를 사용하여 원하는 작업을 수행하고, 응답이 실패한 경우에는 `Logger.logError`를 호출하여 에러 정보를 로그 파일에 기록합니다.

## 로깅 시스템 구현

마지막으로, 실제로 네트워크 에러 정보를 로그 파일에 기록하는 로깅 시스템을 구현해야 합니다. 로깅 시스템은 파일 작성 및 관리, 로그 레벨 설정 등을 포함할 수 있습니다. 이는 각 앱의 요구 사항에 따라 다를 수 있으므로, 자세한 구현 방법은 생략하겠습니다.

위의 코드에서 `Logger.logError` 메서드를 호출한 후에는 로깅 시스템을 사용하여 에러 정보를 로그 파일에 기록하는 코드를 추가해야 합니다.

## 결론

AlamofireNetworkActivityIndicator를 사용하면 네트워크 인디케이터를 편리하게 관리할 수 있습니다. 네트워크 요청 중에 에러가 발생하면 로그 파일에 에러 정보를 기록하여 디버깅 및 문제 해결을 더욱 용이하게 만들 수 있습니다. 로깅 시스템을 구현하여 앱의 로그 관리를 개선할 수도 있습니다.

참고: 
- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)