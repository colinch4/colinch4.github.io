---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator 사용 예제와 동작 원리 설명"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireNetworkActivityIndicator는 Alamofire 라이브러리를 사용하여 네트워크 요청 중에 iOS 디바이스의 상태 표시줄 네트워크 활동 표시기를 자동으로 제어하는 기능을 제공합니다. 이 기능은 사용자에게 네트워크 요청이 진행 중임을 시각적으로 알리고, 사용자 경험을 향상시킵니다.

## 사용 예제

첫 번째로, 앱 내에서 Alamofire 라이브러리를 통해 네트워크 요청을 수행하기 전에 `AlamofireNetworkActivityIndicatorManager.shared.isEnabled` 속성을 `true`로 설정해야 합니다. 이렇게 함으로써 AlamofireNetworkActivityIndicatorManager가 상태 표시줄 네트워크 활동 표시기를 제어하도록 합니다.

```swift
import Alamofire

// 네트워크 요청 전에 인디케이터 활성화
AlamofireNetworkActivityIndicatorManager.shared.isEnabled = true

// Alamofire를 사용하여 네트워크 요청 수행
AF.request("https://api.example.com/data").responseJSON { response in
    switch response.result {
    case .success(let value):
        // 성공적인 응답 처리
        print(value)
    case .failure(let error):
        // 요청 실패 처리
        print(error)
    }
}
```

위의 코드에서 `isEnabled` 속성을 `false`로 설정하면, 상태 표시줄 네트워크 활동 표시기가 동작하지 않게 됩니다.

## 동작 원리

AlamofireNetworkActivityIndicator는 `Alamofire.Session` 클래스의 싱글톤 인스턴스를 통해 네트워크 활동을 감지하고, 상태 표시줄 네트워크 활동 표시기를 제어합니다.

AlamofireNetworkActivityIndicator가 `isEnabled` 속성을 `true`로 설정되면, `Alamofire.Session` 인스턴스는 네트워크 요청 전후에 자동으로 네트워크 활동을 감지합니다. 네트워크 요청이 시작될 때마다, 활동 카운터가 증가하고 네트워크 요청이 완료될 때마다 카운터가 감소합니다. 카운터가 0이 될 때마다 상태 표시줄 네트워크 활동 표시기가 숨겨집니다.

따라서, `AlamofireNetworkActivityIndicatorManager.shared.isEnabled` 속성을 통해 이 기능을 쉽게 활성화 또는 비활성화할 수 있으며, 네트워크 요청을 수행하는 동안 상태 표시줄 네트워크 활동 표시기가 자동으로 제어됩니다.

## 참고 자료

- Alamofire GitHub 레포지토리: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)