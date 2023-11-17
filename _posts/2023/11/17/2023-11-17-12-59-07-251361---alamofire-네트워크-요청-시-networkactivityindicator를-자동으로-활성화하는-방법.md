---
layout: post
title: "[swift] - Alamofire 네트워크 요청 시 NetworkActivityIndicator를 자동으로 활성화하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

애플리케이션에서 Alamofire를 사용하여 네트워크 요청을 처리하고 있다면, NetworkActivityIndicator를 자동으로 활성화하여 사용자에게 현재 네트워크 요청이 진행 중임을 표시할 수 있습니다. 이를 통해 사용자는 애플리케이션이 현재 작업을 수행 중임을 인지하고, 화면이 멈춘 것인지 확인할 수 있습니다.

이번 예제에서는 Alamofire를 사용하여 네트워크 요청을 보내고, 각 요청이 시작할 때 NetworkActivityIndicator를 활성화하고 요청이 완료되면 비활성화하는 방법을 알아보겠습니다.

## 필요한 준비물
1. Swift 프로젝트
2. Alamofire 라이브러리 설치
    - Alamofire는 CocoaPods나 Carthage를 통해 설치할 수 있습니다.

## 네트워크 요청 시 NetworkActivityIndicator 활성화

1. NetworkActivityIndicator를 사용하기 위해 `UIApplication.shared.isNetworkActivityIndicatorVisible` 속성을 사용합니다. 이 속성을 true로 설정하면 인디케이터가 활성화되고, false로 설정하면 비활성화됩니다.

```swift
import Alamofire

Alamofire.request(url).responseJSON { response in
    // 요청이 시작할 때 네트워크 인디케이터를 활성화합니다.
    UIApplication.shared.isNetworkActivityIndicatorVisible = true

    // 요청이 완료되면 네트워크 인디케이터를 비활성화합니다.
    defer {
        UIApplication.shared.isNetworkActivityIndicatorVisible = false
    }

    // 응답을 처리합니다.
    // ...
}
```

위의 예제에서는 Alamofire의 `request` 메서드를 호출하여 네트워크 요청을 보냅니다. 요청이 시작될 때는 `isNetworkActivityIndicatorVisible`를 true로 설정하여 네트워크 인디케이터를 활성화하고, 요청이 완료되면 `defer` 키워드를 사용하여 인디케이터를 비활성화하도록 합니다.

이렇게 하면 네트워크 요청이 시작될 때마다 자동으로 NetworkActivityIndicator가 활성화되고, 요청이 완료되면 비활성화됩니다.

## 결론

Alamofire를 사용하여 네트워크 요청을 처리할 때, NetworkActivityIndicator를 자동으로 활성화하여 사용자에게 현재 작업이 진행 중임을 알릴 수 있습니다. 위의 예제를 참고하여 애플리케이션에 적용해보세요. 

더 자세한 내용은 [Alamofire 홈페이지](https://github.com/Alamofire/Alamofire)를 참고해보시기 바랍니다.