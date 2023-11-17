---
layout: post
title: "[swift] - Alamofire 네트워크 요청 상태에 따라 NetworkActivityIndicator의 색상 변경하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Alamofire는 Swift로 작성된 네트워킹 라이브러리입니다. 애플리케이션에서 네트워크 요청이 진행되고 있을 때 NetworkActivityIndicator (네트워크 활동 인디케이터)를 사용할 수 있습니다. 기본적으로 위치는 상단 상태 표시줄에 위치하며, 흰색으로 표시됩니다.

이제 네트워크 요청의 상태에 따라 NetworkActivityIndicator의 색상을 변경하는 방법을 알아보겠습니다. 

## 필요한 라이브러리 가져오기

먼저 Alamofire 라이브러리를 프로젝트에 추가해야합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. Podfile에 다음 줄을 추가하고 터미널에서 'pod install' 명령을 실행하여 라이브러리를 설치하세요.

```
pod 'Alamofire'
```

프로젝트를 열고 import 구문을 사용하여 Alamofire를 가져옵니다.

```swift
import Alamofire
```

## NetworkActivityIndicatable 프로토콜 사용하기

NetworkActivityIndicator를 색상 변경을 지원하도록 하려면, `NetworkActivityIndicatable` 프로토콜을 구현하는 확장(extension)을 작성해야합니다. 

```swift
extension NetworkActivityIndicatable {

    func updateNetworkActivityIndicatorColor(to color: UIColor) {
        NetworkActivityIndicatorManager.shared.isEnabled = true
        NetworkActivityIndicatorManager.shared.startAnimation()
        NetworkActivityIndicatorManager.shared.tintColor = color
    }
}
```

위의 코드는 `NetworkActivityIndicatorManager`를 사용하여 인디케이터의 활성화 여부와 색상을 설정합니다. `updateNetworkActivityIndicatorColor(to:)` 함수를 호출하면 NetworkActivityIndicator의 색상이 변경됩니다.

## NetworkRequestInterceptor 사용하기

`NetworkRequestInterceptor`는 Alamofire 요청 전에 실행되는 인터셉터(Interceptor)입니다. 이를 사용하면 요청을 수정하거나, 로그를 남기는 등의 작업을 할 수 있습니다. 

```swift
class CustomNetworkRequestInterceptor: NetworkRequestInterceptor {

    func adapt(_ urlRequest: URLRequest) throws -> URLRequest {
        // 네트워크 요청 전에 실행되는 로직을 작성하세요

        // 예를 들어, 요청의 상태에 따라 NetworkActivityIndicator의 색상 변경
        let color: UIColor

        switch urlRequest.url?.host {
            // 요청이 특정 도메인에 대한 것인지 확인
        case "example.com":
            color = .green
        default:
            color = .red
        }

        updateNetworkActivityIndicatorColor(to: color)

        return urlRequest
    }
}
```

위의 예제에서는 `adapt(_:)` 함수에서 NetworkActivityIndicator의 색상을 변경하고 있습니다. 요청 URL의 호스트에 따라 색상이 결정됩니다.

## 네트워크 요청 전에 인터셉터 등록하기

마지막으로 `Alamofire`에서 사용할 인터셉터를 등록해야합니다.

```swift
let interceptor = CustomNetworkRequestInterceptor()
Alamofire.Session(configuration: .default, interceptor: interceptor)
```

위의 코드에서 인스턴스를 생성한 뒤, `Alamofire.Session`을 통해 인터셉터를 등록합니다.

이제 네트워크 요청의 상태에 따라 NetworkActivityIndicator의 색상이 변경됩니다. 이를 통해 애플리케이션에서 네트워크 활동을 더 시각적으로 표시할 수 있습니다.

## 참고 자료

- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)