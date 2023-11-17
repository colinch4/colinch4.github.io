---
layout: post
title: "[swift] - Alamofire를 사용한 네트워크 요청시에만 NetworkActivityIndicator를 활성화하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Alamofire는 Swift에서 네트워크 요청을 보낼 때 많이 사용되는 라이브러리입니다. 네트워크 요청이 진행 중일 때 사용자에게 알리기 위해 iOS 기기의 NetworkActivityIndicator를 활성화할 수 있습니다. 이 글에서는 Alamofire를 사용하여 네트워크 요청시에만 NetworkActivityIndicator를 활성화하는 방법에 대해 알아보겠습니다.

## NetworkActivityIndicator와는 무엇인가요?

NetworkActivityIndicator는 iOS 기기의 화면 상단에 있는 작은 회전하는 인디케이터로, 네트워크 활동이 진행 중임을 나타냅니다. 사용자에게 네트워크 요청이 진행 중인지 알려주기 위해 사용됩니다.

## Alamofire와 NetworkActivityIndicator

Alamofire를 사용하여 네트워크 요청을 보낼 때, 기본적으로는 NetworkActivityIndicator가 자동으로 활성화됩니다. 그러나 때로는 특정 상황에서만 활성화되도록 제어하고 싶을 수 있습니다.

Alamofire는 네트워크 요청을 전송하기 전, 전송 중, 전송 후에 대한 콜백 메서드를 제공합니다. 이 콜백 메서드를 사용하여 NetworkActivityIndicator의 활성화 시점을 제어할 수 있습니다.

아래는 Alamofire를 사용하여 네트워크 요청을 보낼 때 NetworkActivityIndicator를 활성화하는 예시 코드입니다.

```swift
import Alamofire

func sendRequest() {
    // 네트워크 요청 시작 시 NetworkActivityIndicator 활성화
    UIApplication.shared.isNetworkActivityIndicatorVisible = true
    
    AF.request("https://www.example.com").response { response in
        // 네트워크 요청 완료 시 NetworkActivityIndicator 비활성화
        UIApplication.shared.isNetworkActivityIndicatorVisible = false
        
        // 요청 처리 로직 작성
        if let error = response.error {
            print("Error: \(error)")
        } else {
            print("Response: \(response)")
        }
    }
}
```

위의 코드에서 `sendRequest` 함수는 네트워크 요청을 보내는 기능을 수행합니다. 요청이 시작되기 전에 `isNetworkActivityIndicatorVisible` 속성을 `true`로 설정하여 NetworkActivityIndicator를 활성화하고, 요청이 완료되면 `false`로 설정하여 비활성화합니다.

이렇게 함으로써, 해당 네트워크 요청이 진행 중일 때만 NetworkActivityIndicator가 활성화되고, 요청이 완료되면 다시 비활성화됩니다.

## 참고 자료

- [Alamofire 공식 GitHub 페이지](https://github.com/Alamofire/Alamofire)