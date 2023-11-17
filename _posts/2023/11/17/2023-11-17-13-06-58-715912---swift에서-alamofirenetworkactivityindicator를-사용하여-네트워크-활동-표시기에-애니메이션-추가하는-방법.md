---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 표시기에 애니메이션 추가하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Alamofire는 많은 iOS 앱에서 네트워킹을 다루는 데 사용되는 인기있는 Swift 라이브러리입니다. AlamofireNetworkActivityIndicator는 Alamofire의 일부로 포함되어 있으며, 네트워크 활동이 있을 때 시스템 상태 바에 애니메이션을 표시하는 기능을 제공합니다. 이 기능은 사용자에게 현재 앱이 네트워크 요청을 처리하고 있음을 시각적으로 알려줄 수 있습니다.

## AlamofireNetworkActivityIndicator 설치

AlamofireNetworkActivityIndicator를 사용하려면 먼저 Alamofire를 프로젝트에 추가해야 합니다. Cocoapods를 사용하는 경우 Podfile에 다음 라인을 추가하고 `pod install`을 실행하여 종속성을 설치합니다.

```swift
pod 'Alamofire'
```

다음으로 AlamofireNetworkActivityIndicator를 추가하기 위해 Podfile에 다음 라인을 추가하고 다시 `pod install`을 실행합니다.

```swift
pod 'AlamofireNetworkActivityIndicator'
```

설치가 완료되면 `import AlamofireNetworkActivityIndicator`를 사용하여 라이브러리를 가져올 수 있습니다.

## AlamofireNetworkActivityIndicator 사용

AlamofireNetworkActivityIndicator를 사용하려면 AppDelegate.swift 파일에서 다음 코드를 추가해야 합니다.

```swift
import AlamofireNetworkActivityIndicator

func applicationDidBecomeActive(_ application: UIApplication) {
    NetworkActivityIndicatorManager.shared.isEnabled = true
}
```

이렇게 하면 앱이 **active** 상태가 될 때마다 네트워크 활동 표시기가 활성화됩니다.

다음으로 Alamofire 요청을 실행하는 곳에서 네트워크 활동 표시기를 사용할 수 있습니다. Alamofire 요청을 보내기 전에 다음 코드를 추가합니다.

```swift
NetworkActivityIndicatorManager.shared.incrementActivityCount()
```

이렇게 하면 네트워크 요청이 발생할 때마다 네트워크 활동 표시기가 활성화됩니다.

마지막으로 Alamofire 요청이 완료되었을 때 네트워크 활동 표시기를 비활성화합니다. Alamofire 요청이 끝난 후 다음 코드를 추가합니다.

```swift
NetworkActivityIndicatorManager.shared.decrementActivityCount()
```

이제 네트워크 활동 표시기가 Alamofire 요청을 처리하는 동안 적절하게 동작합니다. 네트워크 요청이 시작 및 완료될 때마다 애니메이션이 표시되거나 숨겨집니다.

## 참고 자료

- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)