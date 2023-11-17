---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator를 이용하여 네트워크 활동 상태를 실시간으로 모니터링하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

네트워크 요청이나 응답을 처리할 때 사용자에게 활동 상태를 알려주는 것은 매우 중요합니다. Alamofire는 네트워크 활동을 모니터링하기 위한 여러 가지 기능을 제공합니다. 이 중 `AlamofireNetworkActivityIndicator`를 사용하여 실시간으로 네트워크 활동 상태를 모니터링하는 방법에 대해 알아보겠습니다.

## Alamofire 설치하기

`AlamofireNetworkActivityIndicator`를 사용하려면 먼저 Alamofire를 설치해야 합니다. Cocoapods를 사용하여 Alamofire를 설치하는 방법은 다음과 같습니다.

```
pod 'Alamofire'
```

Podfile에 위의 코드를 추가한 뒤 터미널에서 `pod install`을 실행하면 Alamofire가 설치됩니다.

## AlamofireNetworkActivityIndicator 추가하기

`AlamofireNetworkActivityIndicator`는 Alamofire의 네트워크 활동을 모니터링하기 위한 확장 기능입니다. Cocoapods를 사용하여 `AlamofireNetworkActivityIndicator`를 추가하는 방법은 다음과 같습니다.

```
pod 'AlamofireNetworkActivityIndicator'
```

Podfile에 위의 코드를 추가한 뒤 터미널에서 `pod install`을 실행하면 `AlamofireNetworkActivityIndicator`가 설치됩니다.

## 사용하기

`AlamofireNetworkActivityIndicator`를 사용하여 네트워크 활동 상태를 모니터링하려면 다음과 같이 앱의 AppDelegate.swift 파일에 아래 코드를 추가합니다.

```swift
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    NetworkActivityIndicatorManager.shared.isEnabled = true
    return true
}
```

위의 코드는 앱이 시작될 때 `NetworkActivityIndicatorManager`를 활성화합니다. 이제 Alamofire가 네트워크 요청을 시작할 때마다 iOS의 네트워크 활동 표시줄에 인디케이터가 표시됩니다.

## 주의사항

- `AlamofireNetworkActivityIndicator`는 주로 온라인 저장소와 함께 사용되는 iOS 앱의 네트워크 활동을 모니터링하는 데 사용됩니다.
- 네트워크 활동 모니터링 라이브러리는 iOS 13 이상에서만 제공됩니다.

위의 가이드를 따라하면 Swift에서 `AlamofireNetworkActivityIndicator`를 사용하여 네트워크 활동 상태를 실시간으로 모니터링할 수 있습니다. 해당 확장 기능을 사용하여 앱의 사용자에게 네트워크 작업이 진행 중임을 시각적으로 알려줄 수 있습니다.

---

**참고 자료:**

- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)