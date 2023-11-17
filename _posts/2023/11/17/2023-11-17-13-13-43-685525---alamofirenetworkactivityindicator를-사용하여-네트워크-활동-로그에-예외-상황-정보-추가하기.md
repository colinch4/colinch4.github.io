---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 로그에 예외 상황 정보 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 개발 중에 네트워크 요청을 보내고 응답을 받을 때, 사용자에게 네트워크 활동을 시각적으로 표시하는 것은 중요합니다. Alamofire라는 Swift 기반의 HTTP 네트워킹 라이브러리를 사용하면 네트워크 활동을 관리하기가 더욱 쉬워집니다.

하지만 때때로 네트워크 활동을 로깅하고 예외 상황에 대한 정보를 추가하고 싶을 수 있습니다. AlamofireNetworkActivityIndicator를 사용하면 네트워크 활동 로깅에 예외 상황 정보를 추가할 수 있습니다.

## AlamofireNetworkActivityIndicator

AlamofireNetworkActivityIndicator는 Alamofire 라이브러리의 네트워크 요청 및 응답 활동을 모니터링하고 시스템의 상태 표시줄에 네트워크 활동 인디케이터를 표시하는 데 사용됩니다.

일반적으로 이 라이브러리는 네트워크 활동을 시작하거나 완료할 때 자동으로 활성화되며, Backoff 알고리즘을 사용하여 네트워크 활동이 겹치거나 중복되는 경우 활성화된 시간을 자동으로 연장합니다. 그러나 기본 동작에 예외 상황 정보를 추가하려면 몇 가지 추가 작업을 해야합니다.

## 예외 상황 정보 추가하기

다음은 AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 로그에 예외 상황 정보를 추가하는 방법입니다.

### 1. CustomInterceptor 클래스 생성

먼저 CustomInterceptor라는 클래스를 생성하여 예외 상황 정보를 추가할 수 있습니다.

```swift
import Alamofire

class CustomInterceptor: RequestInterceptor {
    func adapt(_ urlRequest: URLRequest, for session: Session, completion: @escaping (Result<URLRequest, Error>) -> Void) {
        // 요청을 수정하고 예외 상황 정보를 추가하는 로직을 구현합니다.
        var modifiedRequest = urlRequest
        modifiedRequest.addValue("Custom-Value", forHTTPHeaderField: "Custom-Header")
        
        completion(.success(modifiedRequest))
    }
}
```

### 2. 네트워크 클라이언트 생성

다음으로 네트워크 클라이언트를 생성하고 CustomInterceptor를 추가합니다.

```swift
import Alamofire

let customInterceptor = CustomInterceptor()

let session = Session(interceptor: customInterceptor)
```

### 3. 네트워크 요청 보내기

마지막으로 네트워크 요청을 보내면서 위에서 생성한 네트워크 클라이언트를 사용합니다.

```swift
session.request("https://api.example.com/users")
    .validate()
    .responseJSON { response in
        // 응답 처리 로직을 구현합니다.
    }
```

### 4. 결과 확인하기

네트워크 요청을 보내고 나면, 시스템 상태 표시줄에 네트워크 활동 인디케이터가 표시되며, 로깅에 예외 상황 정보가 추가됩니다.

## 결론

AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 로그에 예외 상황 정보를 추가하는 방법을 살펴보았습니다. 이를 통해 앱의 네트워크 활동을 모니터링하고 디버깅하는 데 유용하게 활용할 수 있습니다. 자세한 내용은 [Alamofire](https://github.com/Alamofire/Alamofire) 라이브러리의 공식 문서를 참조하시기 바랍니다.