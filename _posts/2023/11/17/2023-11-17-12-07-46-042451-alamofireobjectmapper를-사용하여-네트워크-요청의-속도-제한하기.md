---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 속도 제한하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 AlamofireObjectMapper를 사용하여 네트워크 요청을 보낼 때, 요청 속도를 제한하는 방법에 대해 알아보겠습니다. AlamofireObjectMapper는 Alamofire와 ObjectMapper를 함께 사용하는 라이브러리로, JSON 데이터를 모델 객체로 매핑해주는 기능을 제공합니다.

네트워크 요청의 속도 제한은 서버로부터 받아오는 데이터의 양과 속도를 제한하여 앱이 과도한 리소스를 사용하지 않도록 조절하는데 도움을 줄 수 있습니다.

## 요청 속도 제한 설정하기

AlamofireObjectMapper는 Alamofire의 기능을 그대로 사용할 수 있기 때문에, Alamofire의 `SessionManager`를 사용하여 요청 속도 제한을 설정할 수 있습니다. `SessionManager`는 네트워크 요청을 관리하는 객체로, `Configuration`을 통해 요청에 적용되는 옵션들을 설정할 수 있습니다.

요청 속도 제한을 설정하기 위해서는 `SessionManager`의 `Configuration` 객체에서 `timeoutIntervalForRequest`와 `timeoutIntervalForResource`를 설정해주어야 합니다. `timeoutIntervalForRequest`는 요청이 서버로부터의 응답을 받을 때까지 얼마나 기다릴지를 결정하는 속성이고, `timeoutIntervalForResource`는 네트워킹 작업이 완료되기까지 얼마나 기다릴지를 결정하는 속성입니다.

```swift
import Alamofire
import AlamofireObjectMapper

let configuration = URLSessionConfiguration.default
configuration.timeoutIntervalForRequest = 10 // 10초 동안 서버 응답을 기다림
configuration.timeoutIntervalForResource = 60 // 60초 동안 네트워킹 작업 완료를 기다림

let sessionManager = SessionManager(configuration: configuration)

// 네트워크 요청 예시
sessionManager.request("https://api.example.com/data")
    .validate() // 응답 코드를 검증
    .responseObject { (response: DataResponse<MyModel>) in
        // 모델 객체로 매핑된 데이터 처리
    }
```

위 코드에서 `timeoutIntervalForRequest`를 10으로 설정하였기 때문에, 서버로부터의 응답이 10초를 넘어가면 요청이 취소됩니다.

## 참고 자료

- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)