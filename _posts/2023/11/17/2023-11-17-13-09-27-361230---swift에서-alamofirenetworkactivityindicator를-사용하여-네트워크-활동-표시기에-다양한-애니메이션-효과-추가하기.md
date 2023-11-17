---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 표시기에 다양한 애니메이션 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱에서 네트워킹 작업을 수행할 때, 네트워크 활동 표시기를 추가하여 사용자에게 진행 중인 작업을 시각적으로 알려주는 것은 좋은 사용자 경험을 제공하기 위한 중요한 요소입니다. 이를 위해 Swift에서 AlamofireNetworkActivityIndicator를 사용하는 방법을 알아보겠습니다.

## AlamofireNetworkActivityIndicator란?

AlamofireNetworkActivityIndicator는 네트워크 요청이 진행 중임을 나타내는 시스템 상태 표시줄의 인디케이터를 관리하는 Alamofire의 부가적인 라이브러리입니다. 이 라이브러리를 사용하면 앱이 네트워크 작업을 수행할 때마다 상태 표시줄에 애니메이션 효과가 표시됩니다.

## 설치

AlamofireNetworkActivityIndicator를 사용하기 위해, 먼저 CocoaPods를 사용하여 프로젝트에 의존성을 추가해야 합니다. `Podfile`에 다음 라인을 추가합니다:

```ruby
pod 'AlamofireNetworkActivityIndicator'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다:

```
$ pod install
```

## 사용 방법

1. Alamofire 오브젝트를 만듭니다:

```swift
import Alamofire

let sessionManager = Session()
```

2. AlamofireNetworkActivityIndicator를 초기화합니다:

```swift
import AlamofireNetworkActivityIndicator

let networkActivityIndicatorManager = NetworkActivityIndicatorManager()

// 또는 기본값으로 초기화할 수도 있습니다:
// let networkActivityIndicatorManager = NetworkActivityIndicatorManager.shared
```

3. 앱의 네트워크 작업 시작 시 네트워크 활동 표시기를 활성화합니다:

```swift
networkActivityIndicatorManager.isEnabled = true
```

4. 네트워크 작업을 시작하기 전에 `isEnabled` 속성을 `true`로 설정하여 네트워크 활동 표시기를 활성화하고, 작업이 완료된 후에 `false`로 설정하여 비활성화합니다:

```swift
networkActivityIndicatorManager.isEnabled = true

sessionManager.request(url).responseJSON { response in
    // 네트워크 작업이 완료되었음을 나타내기 위해 네트워크 활동 표시기를 비활성화합니다
    networkActivityIndicatorManager.isEnabled = false
    
    // 응답 처리 로직을 작성합니다
}
```

5. 추가 구성을 원하는 경우, `NetworkActivityIndicatorManager`의 다양한 속성을 설정하여 네트워크 활동 표시기의 동작을 커스터마이즈할 수 있습니다. 예를 들어, `startAnimationDelay` 속성을 사용하여 네트워크 작업이 시작된 직후에 표시기가 활성화되기까지의 지연 시간을 설정할 수 있습니다:

```swift
networkActivityIndicatorManager.startAnimationDelay = 0.1 // 0.1초 지연
```

위의 예시에서는 `Alamofire`와 `AlamofireNetworkActivityIndicator`을 사용하여 Swift 앱에서 네트워크 활동 표시기에 다양한 애니메이션 효과를 추가하는 방법을 알아보았습니다. 이를 통해 사용자에게 진행 중인 네트워크 작업을 시각적으로 알려주는 좋은 사용자 경험을 제공할 수 있습니다.

## 참고 자료

- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)