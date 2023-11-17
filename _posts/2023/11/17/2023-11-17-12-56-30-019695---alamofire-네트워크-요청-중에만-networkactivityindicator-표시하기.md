---
layout: post
title: "[swift] - Alamofire 네트워크 요청 중에만 NetworkActivityIndicator 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 1. 네트워크 인디케이터 설정하기

네트워크 인디케이터는 iOS의 `UIApplication` 클래스의 `networkActivityIndicatorVisible` 프로퍼티를 사용하여 설정할 수 있습니다. 

```swift
UIApplication.shared.isNetworkActivityIndicatorVisible = true
```

위의 코드를 사용하면 네트워크 인디케이터가 화면 상단의 상태 바에 표시됩니다.

## 2. Alamofire로 네트워크 요청하기

이제 Alamofire를 사용하여 네트워크 요청을 보내는 예제 코드를 작성해보겠습니다.

```swift
import Alamofire

func makeNetworkRequest() {
    // 네트워크 요청 전에 네트워크 인디케이터를 표시한다.
    UIApplication.shared.isNetworkActivityIndicatorVisible = true

    // Alamofire를 사용하여 네트워크 요청을 보낸다.
    AF.request("https://api.example.com/data").responseJSON { response in
        // 네트워크 요청이 완료되면 네트워크 인디케이터를 숨긴다.
        UIApplication.shared.isNetworkActivityIndicatorVisible = false

        // 네트워크 요청에 대한 결과를 처리한다.
        switch response.result {
        case .success(let data):
            // 성공적으로 데이터를 받아왔을 때의 처리
            print(data)
        case .failure(let error):
            // 네트워크 요청이 실패했을 때의 처리
            print(error)
        }
    }
}
```

위의 코드에서는 `makeNetworkRequest` 함수를 호출하면 네트워크 요청이 시작됩니다. 네트워크 요청 전에 `UIApplication.shared.isNetworkActivityIndicatorVisible`로 네트워크 인디케이터를 표시하고, 요청이 완료되면 숨깁니다. 네트워크 요청에 대한 결과는 `response.result`에서 처리할 수 있습니다.

## 3. 네트워크 인디케이터 상태 관리하기

앱에서 여러 개의 네트워크 요청을 동시에 보낼 수 있는 경우가 많습니다. 이 경우, 각 요청마다 네트워크 인디케이터를 설정하여 관리해야 합니다. 

따라서, 네트워크 요청을 시작할 때마다 인디케이터를 설정하고, 요청이 끝날 때마다 인디케이터를 숨기는 작업을 해주어야 합니다.

위의 예제 코드에서 이미 요청 전, 요청 후에 인디케이터를 설정 및 숨기는 작업을 하고 있습니다. 이를 통해 각각의 네트워크 요청에 대한 인디케이터 상태를 관리할 수 있습니다.

## 4. 결론

이번 글에서는 Swift 언어와 Alamofire를 사용하여 네트워크 요청 중에만 네트워크 인디케이터를 표시하는 방법에 대해 알아보았습니다. 

네트워크 인디케이터를 사용하면 사용자에게 진행 중인 요청을 알려주어 사용자 경험을 향상시킬 수 있습니다.