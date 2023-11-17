---
layout: post
title: "[swift] - Alamofire를 사용하여 NetworkActivityIndicator를 커스텀하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

네트워크 요청이 처리되는 동안 사용자에게 진행 중임을 알려주는 네트워크 활동 표시기는 모바일 앱에서 중요한 기능입니다. 이번 블로그 포스트에서는 Swift의 Alamofire 라이브러리를 사용하여 네트워크 활동 표시기를 커스텀하는 방법을 알아보겠습니다.

## Alamofire란?

Alamofire는 Swift로 작성된 HTTP 네트워킹 라이브러리로, 네트워크 요청을 보내고 응답을 받는 작업을 단순화시켜줍니다. 네트워크 통신을 위한 기능을 제공하며, 네트워크 활동 표시기의 표시 및 숨김과 같은 추가 기능도 제공합니다.

## NetworkActivityIndicator 활용하기

네트워크 요청이 진행 중일 때 네트워크 활동 표시기를 활성화하고, 요청이 완료되면 비활성화하는 것은 매우 간단합니다. Alamofire에 기본적으로 내장된 `NetworkActivityIndicator`을 사용하면 이 작업을 손쉽게 수행할 수 있습니다.

```swift
// 적절한 위치에서 네트워크 활동 표시기 활성화하기
Alamofire.NetworkActivityIndicatorManager.shared.isEnabled = true

// 네트워크 요청 완료 후 네트워크 활동 표시기 비활성화하기
Alamofire.NetworkActivityIndicatorManager.shared.isEnabled = false
```

위의 코드에서는 `Alamofire.NetworkActivityIndicatorManager.shared.isEnabled` 속성을 사용하여 네트워크 활동 표시기를 활성화하거나 비활성화할 수 있습니다. 이 코드를 사용하면 앱의 네트워크 요청 상태에 따라 자동으로 네트워크 활동 표시기를 제어할 수 있습니다.

## 커스텀 네트워크 활동 표시기 생성하기

네트워크 활동 표시기를 커스텀하려면 `NetworkActivityIndicatorManager` 클래스를 서브클래싱하여 사용자 정의 동작을 구현해야합니다.

```swift
import Alamofire

class CustomNetworkActivityIndicatorManager: NetworkActivityIndicatorManager {

    static let shared = CustomNetworkActivityIndicatorManager()

    override init() {
        super.init()
        // 커스텀 동작 초기화
    }

    override func incrementActivityCount() {
        super.incrementActivityCount()
        // 커스텀 동작 추가
    }

    override func decrementActivityCount() {
        super.decrementActivityCount()
        // 커스텀 동작 추가
    }
}
```

위의 코드는 `NetworkActivityIndicatorManager`를 상속받은 `CustomNetworkActivityIndicatorManager`를 정의한 예시입니다. `incrementActivityCount()`와 `decrementActivityCount()` 메서드를 오버라이드하여 원하는 동작을 추가할 수 있습니다.

이제 커스텀 네트워크 활동 표시기를 사용하려면 다음과 같이 코드를 수정합니다.

```swift
CustomNetworkActivityIndicatorManager.shared.isEnabled = true
CustomNetworkActivityIndicatorManager.shared.startAnimating()

// 네트워크 요청 완료 후 네트워크 활동 표시기 비활성화하기
CustomNetworkActivityIndicatorManager.shared.stopAnimating()
CustomNetworkActivityIndicatorManager.shared.isEnabled = false
```

위의 코드에서는 `CustomNetworkActivityIndicatorManager`를 사용하여 네트워크 활동 표시기를 활성화하고 사용자 정의 동작을 수행합니다.

## 결론

Alamofire를 사용하여 네트워크 활동 표시기를 커스터마이징하는 방법을 알아보았습니다. 기본적으로 제공되는 `NetworkActivityIndicator`을 사용하거나, `NetworkActivityIndicatorManager`를 서브클래싱하여 커스텀 동작을 추가할 수 있습니다. 앱의 요구에 맞게 활용하여 사용하면 좀 더 효과적인 네트워킹을 구현할 수 있습니다.

더 자세한 내용은 [Alamofire 공식 문서](https://github.com/Alamofire/Alamofire)를 참조하시기 바랍니다.